from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.postgres import Postgres
from pandas import DataFrame
from os import path
import pandas as pd

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_postgres(df: DataFrame, **kwargs) -> None:
    """
    Export data to PostgreSQL, partitioned by year into separate tables.
    Each table is named as 'police_<year>', e.g., 'police_2020', 'police_2021'.
    """
    # Ensure the incident_datetime column is in datetime format
    df['incident_datetime'] = pd.to_datetime(df['incident_datetime'], errors='coerce')

    # Drop rows where incident_datetime could not be converted
    df = df.dropna(subset=['incident_datetime'])

    # Extract year from incident_datetime
    df['year'] = df['incident_datetime'].dt.year

    # Specify configuration for the database connection
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'
    
    # Connect to PostgreSQL and export data by year
    with Postgres.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        for year, data in df.groupby('year'):
            # Define table name for the current year
            table_name = f'police_{year}'
            
            # Export data for the current year to the respective table
            loader.export(
                data.drop(columns=['year']),  
                schema_name='policedb',
                table_name=table_name,
                index=False,
                if_exists='append' 
            )
