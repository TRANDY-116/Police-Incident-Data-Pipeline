import io
import os
import pandas as pd
import requests

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Load only records from the API for events occurring in 2019.
    """
    # Define the URL with a $where clause to limit data to 2019
    url = (
        "https://data.sfgov.org/resource/wg3w-h783.json?$limit=5000000"
        "&$where=incident_datetime >= '2019-01-01T00:00:00.000' "
        "AND incident_datetime < '2020-01-01T00:00:00.000'"
    )

    response = requests.get(url)
    data = pd.read_json(io.StringIO(response.text))

    # Print columns for debugging purposes
    print("Columns in the dataset:", data.columns)

    # Check if data is available and return it
    if not data.empty:
        return data
    else:
        raise ValueError("No data found for the specified time range (2019).")


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    assert not output.empty, 'The output data is empty'
    # Optional: Add more assertions to validate the data range is within 2019
