import numpy as np
from utils.load_data import load_dataset
from utils.eia_codes import name_to_code, date_to_code


class EClass:
    
    """
    Collect energy consumption data for a user-defined energy source.
    
    Retrieves data from the specified energy source according to specific 
    attributes, such as energy consumed per decade, per year, or all years in 
    which more than a certain amount of energy was consumed from that source.
    Use this class to extract and return pure data from the dataset.
    """
    
    def __init__(self,energy_source,dataset=np.empty(0)):
        """
        Receive energy source (as numeric code) and collect corresponding data.
        
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
        if np.size(dataset) == 0:
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
        
        self.freq_errmsg = '"{}" is not a frequency compatible with this dataset; see documentation for permissible frequencies.' 
        self.extr_errmsg = '"{}" is not a recognized input for an extrema; try "max" or "min"' 

    def _daterange(self,start_date,end_date):
        """
        Resize the dataset to cover only the date range specified.
        
        Parameters
        ----------
        start_date, end_date : int
            The dataset start/end dates (both inclusive) as integers (YYYYMM).
            
        Returns
        -------
        bound_data : ndarray
            A 2 column array corresponding to the specified date range.
        """
        # Use dataset default dates unless otherwise specified by the user
        start_date = self.idate if start_date == None else date_to_code(str(start_date))
        end_date = self.fdate if end_date == None else date_to_code(str(end_date))
       
        # Adjust dataset boundaries 
        half_bounded_data = self.data[self.data[:,0] >= start_date]
        bounded_data = half_bounded_data[half_bounded_data[:,0] <= end_date]
        return bounded_data
     
    def _monthlydata(self,data):
        """
        Limit the data to consider only monthly totals.

        Parameters
        ----------
        data : ndarray
            A 2 column array with data to be filtered according to monthly totals.

        Returns
        -------
        monthly_data : ndarray
            A 2 column array corresponding to only the monthly totals.
        """
        # Remove dates where the fifth and sixth digits of the date code are not in 01-12
        month_codes = np.array([int(float(str(date_code)[4:6])) for date_code in data[:,0]])
        monthly_data = data[month_codes!=13]
        return monthly_data
     
    def _yearlydata(self,data):
        """
        Limit the data to consider only yearly totals.

        Parameters
        ----------
        data : ndarray
            A 2 column array with data to be filtered according to yearly totals.

        Returns
        -------
        yearly_data : ndarray
            A 2 column array corresponding to only the yearly totals.
        """
        # Remove dates where the fifth and sixth digits of the date code are not 13 (denoting yearly total)
        month_codes = np.array([int(float(str(date_code)[4:6])) for date_code in data[:,0]])
        yearly_data = data[month_codes==13]
        return yearly_data
       
    def totals(self,freq='yearly',start_date=None,end_date=None,):
        """
        Get the energy consumption totals over a given period.
        
        Parameters
        ----------
        freq : str
            The frequency for gathering totals ('monthly','yearly',or 'cumulative').
        start_date, end_date : str
            The user specified dataset starting and ending dates (both inclusive); 
            acceptable formats are 'YYYYMM', 'YYYY-MM', or 'MM-YYYY'. Dashes ("-") can 
            be substituted for periods ("."), underscores ("_"), or forward slashes ("/").
            
        Returns
        -------
        totals_array : ndarray
            A 2 column array giving dates at the given frequency and corresponding totals.
        """
        freq = freq.lower()

        # Bound data by start and end dates
        totals_data = self._daterange(start_date,end_date)
        
        # Extract data according to frequency
        if freq == 'monthly':
            totals_data = self._monthlydata(totals_data)
        elif freq == 'yearly':
            totals_data = self._yearlydata(totals_data)
        elif freq == 'cumulative':
            # Create a numpy array (1x2) of the energy source's cumulative total
            month_codes = np.array([int(float(str(date_code)[4:6])) for date_code in totals_data[:,0]])
            date_indices_to_sum = (month_codes == 13)
            for i in range(len(date_indices_to_sum)):
                if date_indices_to_sum[-i-1] == False:
                    date_indices_to_sum[-i-1] = True
                else: break
            totals_data = np.array([np.sum(self.data[date_indices_to_sum],axis=0)])
            totals_data[-1,0] = self.data[-1,0]
        else:
            raise ValueError(self.freq_errmsg.format(freq))
        totals_array = totals_data
        return totals_array
        
    def extrema(self,extremum,freq,start_date=None,end_date=None):
        """
        Get the maximum/minimum energy consumed over a given period.
        
        Parameters
        ----------
        extremum : str
            The exteme value to be found ('max' or 'min).
        freq : str
            The frequency for checking extrema ('monthly' or 'yearly').
        start_date, end_date : str
            The user specified dataset starting and ending dates (both inclusive); 
            acceptable formats are 'YYYYMM', 'YYYY-MM', or 'MM-YYYY'. Dashes ("-") can 
            be substituted for periods ("."), underscores ("_"), or forward slashes ("/").
        
        Returns
        -------
        extremum_array : ndarray
            A 1x2 array giving the extremum values specified (column 2) and the date of
            occurrence for that value (column 1).
        """
        # Bound data by start and end dates
        extrema_data = self._daterange(start_date,end_date)

        # Extract data according to frequency
        if freq == 'monthly':
            extremum_data = self._monthlydata(extrema_data)
        elif freq == 'yearly':
            extremum_data = self._yearlydata(extrema_data)
        else:
            raise ValueError(self.freq_errmsg.format(freq))
        
        # Select max or min
        extremum = extremum.lower()[:3]
        if extremum == 'max':
            extremum_array = np.array([extremum_data[np.argmax(extremum_data[:,1])]])
        elif extremum == 'min':
            extremum_array = np.array([extremum_data[np.argmin(extremum_data[:,1])]])
        else:
            raise ValueError(self.extr_errmsg.format(extremum))
        return extremum_array

    #def more_than(self,amount,start_date,end_date,interval):
        """
        Get data for time interval where more than the given amount of energy was consumed.
        
        Parameters
        ----------
        amount: float
            The lower boundary (exclusive) for which data may be included in the dataset.
        start_date, end_date : str
            The user specified dataset starting and ending dates (both inclusive); 
            acceptable formats are 'YYYYMM', 'YYYY-MM', or 'MM-YYYY'. Dashes ("-") can 
            be substituted for periods ("."), underscores ("_"), or forward slashes ("/").
        interval : str
            The time intervals considered for extrema comparison ('yearly',or 'monthly').
        """
        
    
    
    """
    Additonal potential options to add:
        - average yearly energy consumed
        - average seasonal energy consumed
        - consolidate date range selection and monthly/yearly/cumulative selection into a _formatdata method
    """
 

