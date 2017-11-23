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
import pandas as pd
import os
from glob import glob

def load_dataset(dataset_date='default',dataset_type=None):
    """
    Loads an EIA MER dataset from a csv file.
    
    Parameters
    ----------
    dataset_date : str
        The date identifier of the dataset; 'default' and 'newest' are current
        options (the ability to call specific dataset dates to be added).
    dataset_type : str
        The type of dataset to be selected; can be either 'production', 
        'consumption', 'import', or 'export' (set as None for default dataset) 
    
    Returns
    -------
    data_df : DataFrame
        Data from the EIA MER dataset; dataframe contains 3 columns: the date,
        the energy quantitity in quadrillion BTUs, and the code denoting energy
        type
    """
    # Get the dataset corresponding to the date identifier given
    EIA_MER_DATA_PATH = os.getcwd()+'/../data/'
    if dataset_date == 'default': EIA_MER_DATA_FILE = get_default()
    elif dataset_date == 'newest': EIA_MER_DATA_FILE = get_newest(dataset_type)
    else: raise ValueError('"Default" and "Newest" are the only dataset date identifiers currently implemented.')

    # Process the dataset to allow conversion to float
    FULL_PATH = EIA_MER_DATA_PATH+EIA_MER_DATA_FILE
    data_df = pd.read_csv(FULL_PATH,na_values='Not Available')
    data_df = data_df[['YYYYMM','Value','Column_Order']]
    data_df = data_df.rename(index=str,columns={'YYYYMM':'Date','Value':'Value [QBTU]','Column_Order':'ECode'})
    return data_df

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
    labeldict = {'production':'prod',
                 'consumption':'cons',
                 'import':'imp',
                 'export':'exp'}
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


