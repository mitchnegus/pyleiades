"""
Load EIA Monthly Energy Review (MER) datasets.

Functions
---------
load_dataset
    Loads an EIA MER dataset from a csv file.
get_default
    Finds the default MER dataset csv file.
find_most_recent
    Finds the most MER dataset csv file.
"""
import numpy as np


def load_dataset(dataset_date='default',dataset_type=None):
    """
    Loads an EIA MER dataset from a csv file.
    
    Parameters
    ----------
    dataset_date : str
        The date identifier of the dataset; 'default' and 'newest' are current options
        (specific dataset dates to be added).
    dataset_type : str
        The type of dataset to be selected; can be either 'production', 'consumption', 
        'import', or 'export' (set as None for default dataset) 
    
    Returns
    -------
    ndarray
        Data from the EIA MER dataset.
    """
    EIA_MER_DATA_PATH = '/Users/mitch/Documents/Energy_Analysis/enviro/'
    if dataset_date == 'default': EIA_MER_DATA_FILE = get_default()
    #elif dataset_date == 'newest': EIA_MER_DATA_FILE = get_newest()
    else: raise ValueError('"Default" is the only dataset date identifier currently implemented.')
    return np.genfromtxt(EIA_MER_DATA_PATH+EIA_MER_DATA_FILE,float,delimiter=',')[1:,1:4]


def get_default():
    """
    Gets the filename of the default dataset from your filesystem.
    
    Returns
    -------
    str
        The filename of the default dataset.
    """
    return 'EIA_MER.csv'


def get_newest():
    """
    Gets the filename of the most recent dataset from your filesystem.
    
    Returns
    -------
    str
        The filename of the most recently downloaded dataset.
    """
    print('Currently unimplemented.')

