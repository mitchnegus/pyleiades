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


def load_dataset(dataset_label='default'):
    """
    Loads an EIA MER dataset from a csv file.
    
    Parameters
    ----------
    dataset_label : str
        The identifier of the dataset; 'default' and 'newest' are current options
        (specific dataset dates to be added).
        
    Returns
    -------
    ndarray
        Data from the EIA MER dataset.
    """
    EIA_MER_DATA_PATH = '/Users/mitch/Documents/Energy_Analysis/enviro/'
    if dataset_label == 'default': EIA_MER_DATA_FILE = get_default()
    #elif dataset_label == 'newest': EIA_MER_DATA_FILE = get_newest()
    else: raise ValueError('"Default" is the only dataset label currently implemented.')
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

