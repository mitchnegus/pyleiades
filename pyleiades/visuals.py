import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from pyleiades.energies import Energy
from pyleiades.utils import inspection

class Visual:
    """
    Create visuals based on energy data.

    Takes one or more energy histories as input upon initialization, providing
    methods to visualize the data (including the ability to make comparisons
    across energy sources if more than one energy is given. Visualizations
    include histograms, line graphs, pie charts, and animations.

    Attributes
    ––––––––––
    data : DataFrame, optional
        The EIA dataset on which visualizations are based.
    stat_type : str
        The type of statistic ('production', 'consumption', 'import' or
        'export').
    data_date : str
        The date identifier of the dataset. (The default value is `None`, which
        automatically uses the most recently downloaded dataset.)
    energies : list of Energy object
        A list of energies from the dataset to be visualized.

    Parameters
    ––––––––––
    energy_types : str or list of str, optional
        A list of one or more energies to be displayed.
    data : DataFrame, optional
        The EIA dataset to be used. Must be three columns: date, energy
        quantity, and energy code. If omitted, use the default dataset.
    stat_type : str
        The type of statistic to be displayed ('production', 'consumption',
        'import', or 'export').
    data_date : str
        The date identifier of the dataset. (The default value is `None`, which
        automatically uses the most recently downloaded dataset.)
    """

    def __init__(self, energy_types=None, data=None, stat_type='consumption',
                 data_date=None):
        self.data = data
        self.stat_type = stat_type
        self.data_date = data_date
        self.energies = []
        if energy_types is not None:
            if type(energy_types) is str:
                self.include_energy(energy_types)
            elif type(energy_types) is list:
                self.include_energy(*energy_types)
            else:
                raise ValueError("The input energy type(s) must be a single "
                                 "string or a list.")

        self._empty_errmsg = ("No energy histories have been chosen yet for "
                              "the visual.")
        self._freq_errmsg = ("Frequency '{}' is not compatible with this "
                             "visual; see documentation for permissible "
                             "frequency values.")

    def include_energy(self, *energy_types):
        """
        Include energy source(s) in the visual.

        Parameters
        ––––––––––
        energy_types : str
            The type(s) of energy source to be pulled from the dataset.
        """
        for energy_type in energy_types:
            energy = Energy(energy_type, data=self.data,
                            stat_type=self.stat_type, data_date=self.data_date)
            self.energies.append(energy)

    def linegraph(self, ax=None, freq='yearly', start_date=None,
                  end_date=None,):
        """
        Make a line graph of the chosen energy source histories.

        Parameters
        ––––––––––
        freq : str
            The frequency for plotting data points ('monthly' or 'yearly').
        start_date, end_date : str
            The user specified starting and ending dates for the dataset
            (both inclusive); for 'monthly', acceptable formats are 'YYYYMM',
            'YYYY-MM', or 'MM-YYYY' (dashes can be substituted for periods,
            underscores, or forward slashes); for 'yearly' or 'cumulative',
            give only the full year, 'YYYY'.
        ax : Axes object, optional
            A set of axes on which to draw the visual. (If not provided, a new
            set of axes are created.)
        """
        # Input checks
        if len(self.energies) == 0:
            raise RuntimeError(self._empty_errmsg)
        if freq not in ('monthly', 'yearly'):
            raise ValueError(self._freq_errmsg.format(freq))

        # Get data for the selected subject and merge into one dataframe
        totals = pd.DataFrame()
        for energy in self.energies:
            energy_totals = energy.totals(freq, start_date, end_date)
            energy_totals.rename(index=str,
                                 columns={'value': energy.energy_type},
                                 inplace=True)
            totals = pd.concat([totals, energy_totals], axis=1)
        dates = totals.index

        # Generate the plot
        if ax is None:
            fig, ax = plt.subplots(figsize=(10,6))
        for column in totals.columns:
            npoints = len(totals)
            ax.plot(range(npoints), totals[column], label=column)
        ax.legend()
        ax.set_title(f'Energy {self.stat_type} ({freq})')
        ax.set_ylabel('Energy [QBTU]')
        ax.set_xlim(0, npoints)
        if freq == 'yearly':
            interval = 10
        elif freq == 'monthly':
            interval = 120
        xticks, xticklabels = configure_tickmarks(dates, interval)
        ax.set_xticks(xticks)
        ax.set_xticklabels(xticklabels)
        return ax

def configure_tickmarks(labels, interval):
    """
    Given labels and a set interval, generate tickmarks and ticklabels.

    Parameters
    ––––––––––
    labels : list
        The complete list of tickmark labels.
    interval : int
        The step size to use between tickmarks.

    Returns
    –––––––
    ticks : sequence
        A sequence of values to use as tickmarks.
    ticklabels : sequence
        A sequence of values to use as tickmark labels.
    """
    labels = list(labels)
    ticks = range(0, len(labels), interval)
    if len(labels[0]) == 6:
        labels = [f'{_[-2:]}/{_[:-2]}' for _ in labels]
    ticklabels = labels[::interval]
    return ticks, ticklabels

