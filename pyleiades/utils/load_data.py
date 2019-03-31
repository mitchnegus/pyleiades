"""
Utilities for loading EIA Monthly Energy Review (MER) datasets.

Functions
–––––––––
load_dataset
    Loads an EIA MER dataset from a csv file.
"""
import os
import numpy as np
import pandas as pd
from glob import glob
from pyleiades import DATA_DIR, ARCHIVE_DIR

def load_dataset(dataset_date=None, dataset_type=None):
    """
    Loads an EIA MER dataset from a csv file.

    Parameters
    ––––––––––
    dataset_date : str
        The date identifier of the dataset; 'default' and 'newest' are current
        options (the ability to call specific dataset dates to be added).
    dataset_type : str
        The type of the dataset to be selected; can be either 'production',
        'consumption', 'import', or 'export' (set as None for default dataset).

    Returns
    –––––––
    data_df : DataFrame
        Data from the EIA MER dataset; dataframe contains 3 columns: the date,
        the energy quantitity in quadrillion BTUs, and the code denoting energy
        type
    """
    # Get the dataset file corresponding to the date identifier given
    if dataset_date is None:
        data_dir = DATA_DIR
    else:
        data_dir = _find_directory_for_date(dataset_date)
    if dataset_type is None:
        dataset_type = 'consumption'
    data_path = _find_dataset(data_dir, dataset_type)
    # Load and process the dataset file
    data_df = pd.read_csv(data_path, na_values='Not Available',
                          dtype={'YYYYMM': str})
    data_df = _format_dataset(data_df)
    return data_df

def _find_directory_for_date(date):
        """Find the archived directory for a given date, if it exists."""
        dated_dir = f'{ARCHIVE_DIR}/EIA_MER_{date}'
        if os.path.isdir(dated_dir):
            return dated_dir
        else:
            raise ValueError(f"The dataset for the date '{date}' could not be "
                              "found.")

def _find_dataset(data_dir, type):
    """Find the filename for the given dataset type, if it exists."""
    data_filename = f'EIA_MER_{dataset_type}'
    data_path = f'{data_dir}/{data_filename}'
    if os.path.isfile(data_path):
        return data_path
    else:
        raise ValueError(f"The '{type}' type dataset could not be found.")

def _format_dataset(data_df):
    """Format the dataset for further analysis."""
    column_mapping = {'YYYYMM': 'date_code',
                      'Value': 'value',
                      'Column_Order': 'energy_code'}
    data_df = data_df[column_mapping.keys()].dropna()
    data_df = data_df.rename(index=str, columns=column_mapping)
    return data_df
