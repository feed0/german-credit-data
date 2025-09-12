"""
utils/data_utils.py

Utility functions for data processing in the German Credit Data project.
"""
import pandas as pd
from typing import Dict

"""
    Map values in a DataFrame column in-place using a provided mapping.

    Args:
        df (pd.DataFrame): The DataFrame to modify.
        column (Tuple[str, str]): The (label, description) tuple for the column to map.
        value_map (dict): A dictionary mapping original values to new values.

    Returns:
        None. The DataFrame is modified in-place.
"""
def map_column_inplace(df: pd.DataFrame, column: str, value_map: Dict) -> None:
    df[column] = df[column].map(value_map)

"""
    Used to map the german credit data boolean columns to 
    actual booleans.
"""
column_map = {
    'A19 - Telephone': {
        'A191': False,
        'A192': True,
    },
    'A20 - Foreign worker': {
        'A201': True,
        'A202': False,
    },
    'T1 - Is good credit': {
        1: True,
        2: False,
    },
}

"""
    Ordinal column mapping."""
# ## 3 Finally convert the ordinal column ---------------------------------------------------------------------------

# ### 3.1. Define the order of your categories
# installment_categories = [1, 2, 3, 4]

# ### 3.2 Create the custom ordinal data type
# ordinal_dtype = CategoricalDtype(categories=installment_categories, ordered=True)

# ### 3.2 Apply the new data type to the column
# ORDINAL_COLUMN = ('A8', 'Installment rate in percentage of disposable income')
# german_credit_data[ORDINAL_COLUMN] = german_credit_data[ORDINAL_COLUMN].astype(ordinal_dtype)