import io
import os  # Added import for os
import pandas as pd
import requests
from datetime import datetime

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

# File to store the latest timestamp loaded
TIMESTAMP_FILE = 'latest_timestamp.txt'


def get_last_timestamp():
    """Retrieve the last stored timestamp from the file."""
    if os.path.exists(TIMESTAMP_FILE):
        with open(TIMESTAMP_FILE, 'r') as f:
            return f.read().strip()
    return None


def save_last_timestamp(timestamp):
    """Save the latest timestamp to a file."""
    with open(TIMESTAMP_FILE, 'w') as f:
        f.write(timestamp)


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Load only new records from the API.
    """
    url = 'https://data.sfgov.org/resource/wg3w-h783.json?$limit=5000'
    last_timestamp = get_last_timestamp()

    # Add filtering to load only records after the last timestamp
    if last_timestamp:
        url += f"&$where=timestamp > '{last_timestamp}'"

    response = requests.get(url)
    data = pd.read_json(io.StringIO(response.text))

    # Check if data is available
    if not data.empty:
        # Save the latest timestamp in the dataset
        latest_timestamp = data['Incident Datetime'].max()
        save_last_timestamp(latest_timestamp)

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
