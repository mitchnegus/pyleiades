class VClass:
    
    """
    Create visuals based on energy data.
    
    Takes one or more EClasses as input upon initialization, providing
    methods to visualize the data (including the ability to make comparisons
    across energy sources if more than one EClass is given. Visualizations 
    include histograms, line graphs, pie charts, and animations.   
    """
    
    def __init__(self,dataset=np.empty(0)):
        """
        Receive energy source(s) and assemble the appropriate class(es).
        
        Parameters
        ----------
        dataset : array_like, optional
            The dataset from which to pull information. Must be three ordered
            columns–date, energy quantity, and energy code–with no headings.
            If omitted, use the default dataset.
        """

    def include_energy(self,*energies):
        pass
