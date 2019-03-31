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
