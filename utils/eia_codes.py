"""
Utilities for converting user inputs into EIA dataset codes.

Functions
---------
name_to_code
    Converts energy names into EIA energy codes.
date_to_code
    Converts date string into EIA data code.
"""


def name_to_code(name):
    """
    Convert an energy source name to its corresponding EIA dataset numeric code.
    
    Parameters
    ----------
    name : str
        The name of an EIA energy or energy group.
        
    Returns
    -------
    name_code : int
        The code corresponding to the energy source provided.
    """
    key_name = name.lower()
    Ecodes = {'coal':1,
              'natural gas':2,
              'petroleum':3,
              'fossil fuel':4,
              'nuclear':5,
              'hydro':6,
              'geothermal':7,
              'solar':8,
              'wind':9,
              'biomass':10,
              'renewable':11,
              'primary':12}
        
    if key_name not in Ecodes:
        raise KeyError('Key "{}" was not found in the EIA dataset; see documentation for implemented energy sources.'.format(key_name))
    else:
        name_code = Ecodes[key_name]
    return name_code


def date_to_code(date):
    """
    Convert an input date to its corresponding EIA dataset numeric date code.
    
    Parameters
    ----------
    date : str
        A date, given in the format 'YYYYMM', 'YYYY-MM', or 'MM-YYYY'. 
        Dashes can be substituted for periods, underscores, or forward slashes.
        
    Returns
    -------
    date_code : int
        The code corresponding to the energy source provided.
    """
    bad_format_err_msg = 'Date "{}" was not given in an acceptable format; try formatting date as "YYYYMM".'.format(date)
    acceptable_separators = ["-",".","/","_"]
    
    # Convert date to code
    if len(date) == 6:
        date_code_string = date
    elif len(date) == 7:
        if date[4] in acceptable_separators:
            date_code_string = date.replace(date[4],'')
        elif date[2] in acceptable_separators:
            date_code_string = (date[3:]+date[:3]).replace(date[2],'')
    else:
        raise ValueError(bad_format_err_msg)
        
    # Check reasonability of date provided
    try:
        year = int(float(date_code_string[0:4]))
        month = int(float(date_code_string[4:6]))
        if year < 1900 or year > 3000:
            raise ValueError('No data exists for this time period.')
        if month > 13:  # 13 denotes full year sum
            raise ValueError('A month must be given as a number 1-12')
        date_code = int(float(date_code_string))
    except:
        raise ValueError(bad_format_err_msg)
    return date_code
