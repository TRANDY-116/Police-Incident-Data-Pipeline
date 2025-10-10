import pendulum
from airflow import DAG
import datetime


with DAG(
    dag_id="fre",
    schedule=datetime.timedelta(days=3),
    start_date = pendulum.datetime(2025, 10, 11, tz="UTC"),
    end_date = pendulum.datetime(2025, 10, 31, tz="UTC"),
):
