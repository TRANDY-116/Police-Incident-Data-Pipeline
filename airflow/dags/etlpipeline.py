import os
import logging
from datetime import datetime, timedelta
from airflow.sdk import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.base_hook import BaseHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
import pandas as pd
import requests
from sqlalchemy import create_engine


default_args = {
    'owner': 'airflow',