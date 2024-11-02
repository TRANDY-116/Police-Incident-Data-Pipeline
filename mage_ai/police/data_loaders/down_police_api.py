import io
import os
import pandas as pd
import requests
from datetime import datetime

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

# File to store the latest "Incident Datetime" loaded
TIMESTAMP_FILE = 'latest_incident_datetime.txt'


def get_last_timestamp():
    """Retrieve the last stored Incident Datetime from the file."""
    if os.path.exists(TIMESTAMP_FILE):
        with open(TIMESTAMP_FILE, 'r') as f:
            return f.read().strip()
    return None


def save_last_timestamp(timestamp):
    """Save the latest Incident Datetime to a file."""
    with open(TIMESTAMP_FILE, 'w') as f:
        f.write(timestamp)


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Load only new records from the API based on Incident Datetime.
    """
    url = 'https://data.sfgov.org/resource/wg3w-h783.json?$limit=5000'
    last_timestamp = get_last_timestamp()

    # Add filtering to load only records after the last Incident Datetime
    if last_timestamp:
        url += f"&$where=incident_datetime > '{last_timestamp}'"

    response = requests.get(url)
    data = pd.read_json(io.StringIO(response.text))

    # Print columns for debugging purposes
    print("Columns in the dataset:", data.columns)

    # Check if data is available
    if not data.empty:
        # Verify the column name here and update as needed
        if 'Incident Datetime' in data.columns:
            latest_timestamp = data['Incident Datetime'].max()
        elif 'incident_datetime' in data.columns:
            latest_timestamp = data['incident_datetime'].max()
        else:
            raise KeyError("Expected column 'Incident Datetime' or 'incident_datetime' not found in the data.")

        save_last_timestamp(latest_timestamp)

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
