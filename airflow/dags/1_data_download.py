from datetime import datetime, timedelta
import requests
import pandas as pd
from airflow import DAG
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.python import PythonOperator
import time

BASE_URL = "https://data.sfgov.org/resource/wg3w-h783.json"

def fetch_monthly_data_to_postgres(year: int, month: int):
    """Fetch data for one month with pagination and load into Postgres."""
    start_date = datetime(year, month, 1)
    end_date = (start_date + timedelta(days=32)).replace(day=1) - timedelta(days=1)
    start_str = start_date.strftime("%Y-%m-%dT00:00:00")
    end_str = end_date.strftime("%Y-%m-%dT23:59:59")
    
    # Check if data already exists for this month
    hook = PostgresHook(postgres_conn_id="postgres_default")
    check_query = f"""
        SELECT COUNT(*) FROM police_incidents 
        WHERE DATE_TRUNC('month', incident_datetime) = '{year}-{month:02d}-01'::date
    """
    
    try:
        existing_count = hook.get_first(check_query)[0]
        if existing_count > 0:
            print(f"Data already exists for {year}-{month:02d} ({existing_count} rows). Skipping.")
            return
    except Exception as e:
        print(f"Could not check existing data (table may not exist yet): {e}")
    
    # Fetch data with pagination
    offset = 0
    limit = 50000
    all_data = []
    
    print(f"Fetching data for {year}-{month:02d}...")
    
    while True:
        query = f"?$where=incident_datetime between '{start_str}' and '{end_str}'"
        query += f"&$limit={limit}&$offset={offset}"
        url = BASE_URL + query
        
        try:
            print(f"  Fetching offset {offset}...")
            response = requests.get(url, timeout=60)
            response.raise_for_status()
            data = response.json()
            
            if not data:
                break
            
            all_data.extend(data)
            print(f"  Retrieved {len(data)} records (total so far: {len(all_data)})")
            
            # If we got fewer records than the limit, we've reached the end
            if len(data) < limit:
                break
            
            offset += limit
            
            # Add small delay to avoid rate limiting
            time.sleep(0.5)
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data at offset {offset}: {e}")
            # If we already have some data, continue with what we have
            if all_data:
                print(f"Continuing with {len(all_data)} records already fetched")
                break
            else:
                raise
    
    if not all_data:
        print(f"No data found for {year}-{month:02d}")
        return
    
    print(f"Total records fetched: {len(all_data)}")
    
    # Convert to DataFrame
    df = pd.DataFrame(all_data)
    
    # Keep all relevant columns from the API
    keep_cols = [
        "row_id", "incident_datetime", "incident_date", "incident_time",
        "incident_year", "incident_day_of_week", "report_datetime",
        "incident_id", "incident_number", "cad_number", "report_type_code",
        "report_type_description", "incident_code", "incident_category", 
        "incident_subcategory", "incident_description", "resolution",
        "intersection", "cnn", "police_district", "analysis_neighborhood",
        "supervisor_district", "supervisor_district_2012",
        "latitude", "longitude", "point", "data_as_of", "data_loaded_at"
    ]
    df = df[[col for col in keep_cols if col in df.columns]]
    
    # Convert datetimes properly
    df["incident_datetime"] = pd.to_datetime(df["incident_datetime"], errors="coerce")
    df["incident_date"] = pd.to_datetime(df["incident_date"], errors="coerce")
    df["report_datetime"] = pd.to_datetime(df["report_datetime"], errors="coerce")
    df["data_as_of"] = pd.to_datetime(df["data_as_of"], errors="coerce")
    df["data_loaded_at"] = pd.to_datetime(df["data_loaded_at"], errors="coerce")
    
    # Convert numeric columns
    if "latitude" in df.columns:
        df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
    if "longitude" in df.columns:
        df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")
    
    # Convert point column to JSON string if it exists (Postgres JSONB)
    if "point" in df.columns:
        df["point"] = df["point"].apply(lambda x: str(x) if pd.notna(x) else None)
    
    # Remove duplicates based on incident_id if it exists
    if "incident_id" in df.columns:
        initial_count = len(df)
        df = df.drop_duplicates(subset=["incident_id"], keep="first")
        if len(df) < initial_count:
            print(f"Removed {initial_count - len(df)} duplicate records")
    
    # Load into Postgres
    try:
        engine = hook.get_sqlalchemy_engine()
        df.to_sql("police_incidents", engine, if_exists="append", index=False, method="multi")
        print(f"✓ Successfully inserted {len(df)} rows for {year}-{month:02d}")
    except Exception as e:
        print(f"Error loading data to Postgres: {e}")
        raise

def generate_monthly_downloads():
    """Loop from 2018-03 till today and load each month."""
    today = datetime.today()
    year, month = 2018, 1
    
    total_months = 0
    successful_months = 0
    failed_months = []
    
    while (year < today.year) or (year == today.year and month <= today.month):
        total_months += 1
        try:
            fetch_monthly_data_to_postgres(year, month)
            successful_months += 1
        except Exception as e:
            print(f"✗ Failed to process {year}-{month:02d}: {e}")
            failed_months.append(f"{year}-{month:02d}")
        
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1
    
    # Summary
    print("\n" + "="*50)
    print(f"SUMMARY: Processed {total_months} months")
    print(f"✓ Successful: {successful_months}")
    if failed_months:
        print(f"✗ Failed: {len(failed_months)}")
        print(f"  Failed months: {', '.join(failed_months)}")
    print("="*50)

# --- Airflow DAG ---
with DAG(
    dag_id="sf_incidents_to_postgres",
    start_date=datetime(2018, 1, 1),
    schedule="@monthly",
    catchup=True,
    tags=["sf_data", "postgres", "api", "etl"],
    default_args={
        "retries": 2,
        "retry_delay": timedelta(minutes=5),
    },
) as dag:
    load_task = PythonOperator(
        task_id="load_sf_incidents_to_postgres",
        python_callable=generate_monthly_downloads,
        execution_timeout=timedelta(hours=2),
    )
    load_task