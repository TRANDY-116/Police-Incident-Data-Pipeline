if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Clean the dataset by dropping unnecessary columns.
    
    Args:
        data: The output from the upstream parent block.
        
    Returns:
        DataFrame: Cleaned dataset with specified columns removed.
    """
    # List of columns to drop
    columns_to_drop = [
        ':@computed_region_26cr_cadq', ':@computed_region_qgnn_b9vv', 
        ':@computed_region_jwn9_ihcz', ':@computed_region_h4ep_8xdi', 
        ':@computed_region_nqbw_i6c3', ':@computed_region_n4xg_c4py', 
        ':@computed_region_jg9y_a9du'
    ]
    
    # Drop columns if they exist in the data
    data_cleaned = data.drop(columns=[col for col in columns_to_drop if col in data.columns], errors='ignore')

    return data_cleaned


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    assert all(
        col not in output.columns for col in [
            ':@computed_region_26cr_cadq', ':@computed_region_qgnn_b9vv', 
            ':@computed_region_jwn9_ihcz', ':@computed_region_h4ep_8xdi', 
            ':@computed_region_nqbw_i6c3', ':@computed_region_n4xg_c4py', 
            ':@computed_region_jg9y_a9du'
        ]
    ), 'Not all specified columns were dropped.'
