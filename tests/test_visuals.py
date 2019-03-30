import numpy as np
from matplotlib import pyplot as plt
from pyleiades.visuals import Visual

class TestVisual:

    def test_include_energy(self,testdata):
        nuclear_E_data = testdata.iloc[7:].Value
        visual = Visual(data_date='test')
        visual.include_energy('nuclear','coal')
        nuc_E_data = visual.energy_data[0].E_data.Value
        assert 'nuclear' == visual.energy_data[0].energy_type
        assert 'coal' == visual.energy_data[1].energy_type
        assert nuc_E_data.equals(nuclear_E_data)

    def test_linegraph_TotalsDefaults(self,testdata):
        valarray = testdata.Value.values
        nuclear_yearly_data = np.array([valarray[7],valarray[20]])
        visual = Visual(data_date='test')
        visual.include_energy('nuclear')
        ax = visual.linegraph('totals')
        nuc_yearly_data = ax.lines[0].get_xydata().T[1]
        assert np.array_equal(nuc_yearly_data,nuclear_yearly_data)
