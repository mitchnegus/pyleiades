import numpy as np
from pyleiades.energies import Energy

class TestEnergy:

    def test_isolate_energy(self, testdata):
        nuc_test_data = testdata.iloc[7:].value
        nuc = Energy('nuclear', stat_type='test')
        nuc_energy_data = nuc.energy_data.value
        assert nuc_energy_data.equals(nuc_test_data)

    def test_monthly_data(self, testdata):
        valarray = testdata.value.values
        nuc_test_data = np.concatenate([valarray[8:20], valarray[21:23]])
        nuc = Energy('nuclear', stat_type='test')
        nuc_monthly_data = nuc.monthly_data.value.values
        assert np.array_equal(nuc_monthly_data, nuc_test_data)

    def test_yearly_data(self, testdata):
        valarray = testdata.value.values
        nuc_test_data = np.array([valarray[7], valarray[20]])
        nuc = Energy('nuclear', stat_type='test')
        nuc_yearly_data = nuc.yearly_data.value.values
        assert np.array_equal(nuc_yearly_data, nuc_test_data)

    def test_daterange_bounding_inputs(self, testdata):
        valarray = testdata.value.values
        nuc_test_date_range = np.concatenate([valarray[10:20], valarray[21:22]])
        nuc = Energy('nuclear', stat_type='test')
        nuc_date_range = nuc._daterange(nuc.monthly_data, '197303', '197401') \
                            .value.values
        assert np.array_equal(nuc_date_range, nuc_test_date_range)

    def test_daterange_bounding_defaults(self, testdata):
        valarray = testdata.value.values
        nuc_test_date_range = np.concatenate([valarray[8:20], valarray[21:23]])
        nuc = Energy('nuclear', stat_type='test')
        nuc_date_range = nuc._daterange(nuc.monthly_data, None, None) \
                            .value.values
        assert np.array_equal(nuc_date_range, nuc_test_date_range)

    def test_totals_monthly(self, testdata):
        valarray = testdata.value.values
        nuc_test_totals = np.concatenate([valarray[8:20], valarray[21:23]])
        nuc = Energy('nuclear', stat_type='test')
        nuc_monthly_totals = nuc.totals('monthly').value.values
        assert np.array_equal(nuc_monthly_totals, nuc_test_totals)

    def test_totals_yearly(self, testdata):
        valarray = testdata.value.values
        nuc_test_totals = np.array([valarray[7], valarray[20]])
        nuc = Energy('nuclear', stat_type='test')
        nuc_yearly_totals = nuc.totals('yearly').value.values
        assert np.array_equal(nuc_yearly_totals, nuc_test_totals)

    def test_totals_cumulative(self, testdata):
        valarray = testdata.value.values
        nuc_test_total = np.sum(np.array([valarray[7], valarray[20]]))
        nuc = Energy('nuclear', stat_type='test')
        nuc_cumulative_total = nuc.totals('cumulative')
        assert nuc_cumulative_total == nuc_test_total

    def test_extrema_maximum_month(self, testdata):
        valarray = testdata.value.values
        nuc_test_max_val = 0.20
        nuc_test_max_month = '197310'
        nuc = Energy('nuclear', stat_type='test')
        nuc_max_month, nuc_max_val = nuc.extrema('max', 'monthly')
        assert nuc_max_month == nuc_test_max_month
        assert nuc_max_val == nuc_test_max_val

    def test_extrema_minimum_month(self, testdata):
        valarray = testdata.value.values
        nuc_test_min_val = 0.09
        nuc_test_min_month = '197303'
        nuc = Energy('nuclear', stat_type='test')
        nuc_min_month, nuc_min_val = nuc.extrema('min', 'monthly')
        assert nuc_min_month == nuc_test_min_month
        assert nuc_min_val == nuc_test_min_val

    def test_extrema_maximum_year(self, testdata):
        valarray = testdata.value.values
        nuc_test_max_val = 1.30
        nuc_test_max_year = '1973'
        nuc = Energy('nuclear', stat_type='test')
        nuc_max_year, nuc_max_val = nuc.extrema('max', 'yearly')
        assert nuc_max_year == nuc_test_max_year
        assert nuc_max_val == nuc_test_max_val

    def test_extrema_minimum_year(self, testdata):
        valarray = testdata.value.values
        nuc_test_min_val = 0.60
        nuc_test_min_year = '1972'
        nuc = Energy('nuclear', stat_type='test')
        nuc_min_year, nuc_min_val = nuc.extrema('min', 'yearly')
        assert nuc_min_year == nuc_test_min_year
        assert nuc_min_val == nuc_test_min_val
