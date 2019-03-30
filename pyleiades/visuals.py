import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from main.energies import Energy


class Visual:
    """
    Create visuals based on energy data.

    Takes one or more energy histories as input upon initialization, providing
    methods to visualize the data (including the ability to make comparisons
    across energy sources if more than one energy is given. Visualizations
    include histograms, line graphs, pie charts, and animations.

    Parameters
    ––––––––––
    data : DataFrame, optional
        The EIA dataset to be used. Must be three columns: date, energy
        quantity, and energy code. If omitted, use the default dataset.
    data_date : str
        The date identifier of the dataset; 'default' and 'newest' are
        current options (the ability to call specific dataset dates to be
        added).
    """

    def __init__(self,data=pd.DataFrame(),data_date='default'):
        self.complete_data = data
        self.data_date = data_date
        self.energy_data = []

        self.empty_errmsg = ('No energy histories have been chosen yet for '
                             'the visual.')
        self.sub_errmsg = ('Subject "{}" is not compatible with this visual; '
                           'see documentation for permissible subjects.')

    def include_energy(self,*energy_type):
        """
        Include energy source(s) in the visual.

        Parameters
        ––––––––––
        energy_type : str
            The type of energy source to be pulled from the dataset.
        """
        for E_type in energy_type:
            self.energy_data.append(Energy(E_type,data_date=self.data_date))

    def linegraph(self,subject,freq='yearly',start_date=None,end_date=None):
        """
        Make a line graph of the chosen energy source histories.

        Parameters
        ––––––––––
        subject : str
            The subject of the line graph ('totals','maxima', or 'minima').
        freq : str
            The frequency for checking extrema ('monthly' or 'yearly').
        start_date, end_date : str
            The user specified starting and ending dates for the dataset
            (both inclusive); for 'monthly', acceptable formats are 'YYYYMM',
            'YYYY-MM', or 'MM-YYYY' (dashes can be substituted for periods,
            underscores, or forward slashes); for 'yearly' or 'cumulative',
            give only the full year, 'YYYY'.
        """
        if len(self.energy_data) == 0:
            raise RuntimeError(self.empty_errmsg)

        # Get data for the selected subject and merge into one dataframe
        if subject == 'totals':
            subject_data = [energy.totals(freq,start_date,end_date)
                            for energy in self.energy_data]
        elif subject == 'maxima':
            subject_data = [energy.extrema('max',freq,start_date,end_date)
                            for energy in self.energy_data]
        elif subject == 'minima':
            subject_data = [energy.extrema('min',freq,start_date,end_date)
                            for energy in self.energy_data]
        else:
            raise ValueError(self.sub_errmsg.format(subject))
        graph_data = pd.concat(subject_data,axis=1)
        graph_data.columns = [energy.energy_type for energy in self.energy_data]
        graph_data.index = graph_data.index.astype(int)

        # Generate the plot
        ax = graph_data.plot()
        ax.set_title('Energy Consumption History')
        if freq == 'yearly':
            ax.set_xticks(graph_data.index[::10])
        elif freq == 'monthly':
            month_ticks = graph_data.index[::120]
            month_labels = [str(t)[-2:]+'/'+str(t)[:-2] for t in month_ticks]
            graph_data.index = graph_data.index.astype(int)
            ax.set_xticks(graph_data.index[::120])
            ax.set_xticklabels(month_labels)
        ax.set_ylabel('Energy [QBTU]')
        return ax
