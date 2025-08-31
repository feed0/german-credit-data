"""
utils/data_utils.py

Utility functions for data processing in the German Credit Data project.
"""
import pandas as pd
from typing import Tuple, Dict

def map_column_inplace(df: pd.DataFrame, column: Tuple[str, str], value_map: Dict) -> None:
    """
    Map values in a DataFrame column in-place using a provided mapping.

    Args:
        df (pd.DataFrame): The DataFrame to modify.
        column (Tuple[str, str]): The (label, description) tuple for the column to map.
        value_map (dict): A dictionary mapping original values to new values.

    Returns:
        None. The DataFrame is modified in-place.
    """
    df[column] = df[column].map(value_map)
