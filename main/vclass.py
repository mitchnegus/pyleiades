class VClass:
    
    """
    Create visuals based on energy data.
    
    Takes one or more EClasses as input upon initialization, providing
    methods to visualize the data (including the ability to make comparisons
    across energy sources if more than one EClass is given. Visualizations 
    include histograms, line graphs, pie charts, and animations.   
    """
    
    def __init__(self,*energies):
