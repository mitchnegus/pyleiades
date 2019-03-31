import numpy as np
from matplotlib import pyplot as plt
from pyleiades.visuals import Visual

class TestVisual:

    def test_include_energy(self, testdata):
        nuc_test_data = testdata.iloc[7:].value
        visual = Visual(stat_type='test')
        visual.include_energy('nuclear', 'coal')
        nuc_energy_data = visual.energies[0].energy_data.value
        assert 'nuclear' == visual.energies[0].energy_type
        assert 'coal' == visual.energies[1].energy_type
        assert nuc_energy_data.equals(nuc_test_data)

    #def test_linegraph_TotalsDefaults(self,testdata):
    #    valarray = testdata.Value.values
    #    nuclear_yearly_data = np.array([valarray[7],valarray[20]])
    #    visual = Visual(data_date='test')
    #    visual.include_energy('nuclear')
    #    ax = visual.linegraph('totals')
    #    nuc_yearly_data = ax.lines[0].get_xydata().T[1]
    #    assert np.array_equal(nuc_yearly_data,nuclear_yearly_data)
