import numpy as np
from main.energies import Energy

class TestEnergy:
    
    def test_IsolateEnergy(self,testdata):
        nuclear_E_data = testdata.iloc[7:].Value
        nuc = Energy('nuclear',data_date='test')
        nuc_E_data = nuc.E_data.Value
        assert nuc_E_data.equals(nuclear_E_data)

    def test_MonthlyData(self,testdata):
        valarray = testdata.Value.values
        nuclear_monthly_data = np.concatenate([valarray[8:20],valarray[21:23]])
        nuc = Energy('nuclear',data_date='test')
        nuc_monthly_data = nuc.monthly_data.Value.values
        assert np.array_equal(nuc_monthly_data,nuclear_monthly_data)

    def test_YearlyData(self,testdata):
        valarray = testdata.Value.values
        nuclear_yearly_data = np.array([valarray[7],valarray[20]])
        nuc = Energy('nuclear',data_date='test')
        nuc_yearly_data = nuc.yearly_data.Value.values
        assert np.array_equal(nuc_yearly_data,nuclear_yearly_data)

    def test_daterange_BoundingInputDates(self,testdata):
        valarray = testdata.Value.values
        nuclear_date_range = np.concatenate([valarray[10:20],valarray[21:22]])
        nuc = Energy('nuclear',data_date='test')
        nuc_date_range = nuc._daterange(nuc.monthly_data,'197303','197401').Value.values
        assert np.array_equal(nuc_date_range,nuclear_date_range)
    
    def test_daterange_BoundingDefaultDates(self,testdata):
        valarray = testdata.Value.values
        nuclear_date_range = np.concatenate([valarray[8:20],valarray[21:23]])
        nuc = Energy('nuclear',data_date='test')
        nuc_date_range = nuc._daterange(nuc.monthly_data,None,None).Value.values
        assert np.array_equal(nuc_date_range,nuclear_date_range)
      
    def test_totals_FindingMonthlyTotals(self,testdata):
        valarray = testdata.Value.values 
        nuclear_monthly_tots = np.concatenate([valarray[8:20],valarray[21:23]])
        nuc = Energy('nuclear',data_date='test')
        nuc_monthly_tots = nuc.totals('monthly').Value.values
        assert np.array_equal(nuc_monthly_tots,nuclear_monthly_tots)
        
    def test_totals_FindingYearlyTotals(self,testdata):
        valarray = testdata.Value.values 
        nuclear_yearly_tots = np.array([valarray[7],valarray[20]])
        nuc = Energy('nuclear',data_date='test')
        nuc_yearly_tots = nuc.totals('yearly').Value.values
        assert np.array_equal(nuc_yearly_tots,nuclear_yearly_tots)

    def test_totals_FindingCumulativeTotal(self,testdata):
        valarray = testdata.Value.values 
        nuclear_cumulative_total = np.sum(np.array([valarray[7],valarray[20]]))
        nuc = Energy('nuclear',data_date='test')
        nuc_cumulative_total = nuc.totals('cumulative')
        assert nuc_cumulative_total == nuclear_cumulative_total

    def test_extrema_FindingMaximumMonth(self,testdata):
        valarray = testdata.Value.values
        nuclear_max_val = 0.20
        nuclear_max_month = '197310'
        nuc = Energy('nuclear',data_date='test')
        nuc_max_month,nuc_max_val = nuc.extrema('max','monthly')
        assert nuc_max_month == nuclear_max_month
        assert nuc_max_val == nuclear_max_val

    def test_extrema_FindingMinimumMonth(self,testdata):
        valarray = testdata.Value.values
        nuclear_min_val = 0.09
        nuclear_min_month = '197303'
        nuc = Energy('nuclear',data_date='test')
        nuc_min_month,nuc_min_val = nuc.extrema('min','monthly')
        assert nuc_min_month == nuclear_min_month
        assert nuc_min_val == nuclear_min_val

    def test_extrema_FindingMaximumYear(self,testdata):
        valarray = testdata.Value.values
        nuclear_max_val = 1.30
        nuclear_max_year = '1973'
        nuc = Energy('nuclear',data_date='test')
        nuc_max_year,nuc_max_val = nuc.extrema('max','yearly')
        assert nuc_max_year == nuclear_max_year
        assert nuc_max_val == nuclear_max_val

    def test_extrema_FindingYearlyMinimum(self,testdata):
        valarray = testdata.Value.values
        nuclear_min_val = 0.60
        nuclear_min_year = '1972'
        nuc = Energy('nuclear',data_date='test')
        nuc_min_year,nuc_min_val = nuc.extrema('min','yearly')
        assert nuc_min_year == nuclear_min_year
        assert nuc_min_val == nuclear_min_val

