import seaborn as sns


class VClass:
    
    """
    Create visuals based on energy data.
    
    Takes one or more EClasses as input upon initialization, providing
    methods to visualize the data (including the ability to make comparisons
    across energy sources if more than one EClass is given. Visualizations 
    include histograms, line graphs, pie charts, and animations.   
    """
    
    def __init__(self,data=pd.DataFrame()):
        """
        Create a class for constructing visuals from a dataset. 
        
        Parameters
        ----------
        data : DataFrame, optional
            The EIA dataset to be used. Must be three columns: date, energy
            quantity, and energy code. If omitted, use the default dataset.
        """
        pass

    def include_energy(self,*energy_source):
        """
        Include energy source(s) in the visual.
        
        Parameters
        ----------
        energy_source : str
            The energy source to be pulled from the dataset.
        """
        pass

    def linegraph(self,subject):
        """
        Make a line graph of the chosen energy source histories.
        
        Parameters
        ----------
        subject : str
            The subject of the line graph ('totals','maximima', or 'minima').
        """
        pass
