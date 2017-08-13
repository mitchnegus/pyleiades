import numpy as np
from load_data import load_dataset
from eia_codes import name_to_code, date_to_code


class EClass:
    
    """
    Collect energy consumption data for a user-defined energy source.
    
    Retrieves data from the specified energy source according to specific 
    attributes, such as energy consumed per decade, per year, or all years in 
    which more than a certain amount of energy was consumed from that source.
    """
    
    def __init__(self,energy_source,dataset=None):
        """
        Receive energy source (as numeric code) and collect corresponding data from the input dataset
        
        Parameters
        ----------
        Ecode : int
            The energy source to be pulled from the dataset.
        dataset : array_like, optional
            The dataset from which to pull information. Must be three ordered columns
            –date, energy quantity, and energy code–with no headings. If omitted, use the
            default dataset.
        """
        # Use default dataset if dataset argument is omitted
        if dataset == None:
            dataset = load_dataset()
        # Determine Ecode from energy source name
        Ecode = name_to_code(energy_source)

        # Eliminate 'nan' data from source
        dataset = dataset[np.logical_not(np.isnan(dataset[:,1]))]
        
        # Isolate this energy's data from source, and remove (now superfluous) Ecode
        self.data = dataset[dataset[:,2]==Ecode,:2]
                
        # Get the oldest and newest datapoint dates for this energy" 
        self.idate = int(min(self.data[:,0]))
        self.fdate = int(max(self.data[:,0]))
    
    def daterange(self,start_date,end_date):
        """
        Resize the dataset to cover only the date range specified.
        
        Parameters
        ----------
        start_date, end_date : int
            The dataset start/end dates (both inclusive) as integers (YYYYMM)
            
        Returns
        -------
        bound_data : ndarray
            A 2 column array corresponding to the specified range.
        """
        half_bounded_data = self.data[self.data[:,0] >= start_date]
        bounded_data = half_bounded_data[half_bounded_data[:,0] <= end_date]
        return bounded_data
        
     
    def totals(self,freq='yearly',start_date=None,end_date=None,):
        """
        Get the energy consumption totals over a given period.
        
        Parameters
        ----------
        start_date, end_date : str
            The user specified dataset starting and ending dates (both inclusive); 
            acceptable formats are 'YYYYMM', 'YYYY-MM', or 'MM-YYYY'. Dashes ("-") can 
            be substituted for periods ("."), underscores ("_"), or forward slashes ("/").
        freq : str
            The frequency for gathering totals ('monthly','yearly',or 'cumulative').
            
        Returns
        -------
        totals_array : ndarray
            A 2 column array giving dates at the given frequency and corresponding totals.
        """
        start_date = self.idate if start_date == None else date_to_code(str(start_date))
        end_date = self.fdate if end_date == None else date_to_code(str(end_date))
        
        # Bound data by start and end dates
        totals_data = self.daterange(start_date,end_date)
        
        # Extract data according to frequency
        month_codes = np.array([int(float(str(date_code)[4:])) for date_code in totals_data[:,0]])
        if freq == 'monthly':
            # Create a numpy array selecting only monthly totals (denoted as YYYYMM where MM is 01-12 in the date_code)
            totals_data = totals_data[month_codes!=13]
        elif freq == 'yearly':
            # Create a numpy array selecting only yearly totals (denoted as YYYY13 in the date_code)
            totals_data = self.data[month_codes==13]
        elif freq == 'cumulative':
            # Create a numpy array (1x2) of the energy source's cumulative total
            date_indices_to_sum = month_codes==13
            for i in range(len(date_indices_to_sum)):
                if date_indices_to_sum[-i-1] == False:
                    date_indices_to_sum[-i-1] = True
                else: break
            totals_data = np.array([np.sum(self.data[date_indices_to_sum],axis=0)])
            totals_data[-1,0] = self.data[-1,0]
        else:
            raise ValueError('"{}" is not a frequency compatible with this dataset; see documentation for permissible frequencies.'.format(freq))
        totals_array = totals_data
        return totals_array
        
    #def extrema(self,extremum,start_date,end_date,interval):
        """
        Get the maximum/minimum energy ever consumed over a given interval.
        
        Parameters
        ----------
        extremum : str
            The exteme value to be found ('max' or 'min).
        start_date, end_date : str
            The user specified dataset starting/ending points; 
            acceptable formats are 'YYYYMMDD', 'YYYY-MM-DD', MM-DD-YYYY', or 'MM/DD/YYYY'.
        interval : str
            The time intervals considered for extrema comparison ('yearly' or 'monthly').
        """


        
    #def more_than(self,amount,start_date,end_date,interval):
        """
        Get data for time interval where more than the given amount of energy was consumed
        
        Parameters
        ----------
        amount: float
            The lower boundary (exclusive) for which data may be included in the dataset.
        start_date, end_date : str
            The user specified dataset starting/ending points; 
            acceptable formats include 'YYYYMMDD', 'MM-DD-YYYY', and 'MM/DD/YYYY'.
        interval : str
            The time intervals considered for extrema comparison ('yearly',or 'monthly').
        """
        
    
    
    """
    Additonal potential options to add:
        - average yearly energy consumed
        - average seasonal energy consumed
    """
 

