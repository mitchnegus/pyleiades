"""
Utilities for loading EIA Monthly Energy Review (MER) datasets.

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
import os
from glob import glob

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
    # Get the dataset corresponding to the date identifier given
    EIA_MER_DATA_PATH = os.getcwd()+'/data/'
    if dataset_date == 'default': EIA_MER_DATA_FILE = get_default()
    elif dataset_date == 'newest': EIA_MER_DATA_FILE = get_newest(dataset_type)
    else: raise ValueError('"Default" is the only dataset date identifier currently implemented.')

    # Process the dataset to allow conversion to float
    data_string_array = np.genfromtxt(EIA_MER_DATA_PATH+EIA_MER_DATA_FILE,dtype=str,delimiter=',')[1:,1:4]
    data_string_array = np.char.replace(data_string_array,'"','')
    data_string_array = np.char.replace(data_string_array,'Not Available','nan')
    data_float_array = data_string_array.astype(float)
    return data_float_array

def get_default():
    """
    Gets the filename of the default dataset from your filesystem.
    
    Returns
    -------
    str
        The filename of the default dataset.
    """
    return 'EIA_MER.csv'


def get_newest(dataset_type):
    """
    Gets the filename of the most recent dataset from your filesystem.
    
    Returns
    -------
    str
        The filename of the most recently downloaded dataset.
    """
    labeldict = {'production':'prod', 'consumption':'cons', 'import':'imp', 'export':'exp'}
    label = labeldict[dataset_type]

    directories = [directory.split('/')[1] for directory in glob('data/*/')]
    dirdates = np.array([int(directory[-6:]) for directory in directories])
    newestdir = directories[np.argmax(dirdates)]
    basename = newestdir.split('/')[-1]
    typelist = basename.split('_')
    typelist.insert(2,label)
    typename = '_'.join(typelist)
    newestdatafile = newestdir+'/'+typename+'.csv'
    return newestdatafile


