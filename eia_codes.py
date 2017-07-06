"""
Provide utilities for working with EIA dataset codes.

Functions
---------
name_to_code
    Converts energy names into EIA energy codes
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
    code : int
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
        raise KeyError('"%s" was not found in the EIA dataset; \
                        see documentation for implemented energy sources')
    else:
        code = Ecodes[key_name]
    return code

