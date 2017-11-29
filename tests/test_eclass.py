import pandas as pd
import numpy as np
from main.eclass import EClass

class TestEClass:
    
    def test_IsolateEnergy(self,testdata):
        E_data = testdata.iloc[7:].Value
        nuc = EClass('nuclear',data_date='test')
        nuc_E_data = nuc.E_data.Value
        assert nuc_E_data.equals(E_data)

    def test_MonthlyData(self,testdata):
        valarray = testdata.Value.values
        monthly_data = np.concatenate([valarray[8:20],valarray[21:23]])
        nuc = EClass('nuclear',data_date='test')
        nuc_monthly_data = nuc.monthly_data.Value.values
        assert np.array_equal(nuc_monthly_data,monthly_data)

    def test_YearlyData(self,testdata):
        valarray = testdata.Value.values
        yearly_data = np.array([valarray[7],valarray[20]])
        nuc = EClass('nuclear',data_date='test')
        nuc_yearly_data = nuc.yearly_data.Value.values
        assert np.array_equal(nuc_yearly_data,yearly_data)

    def test_daterange_BoundingInputDates(self,testdata):
        valarray = testdata.Value.values
        date_range = np.concatenate([valarray[10:20],valarray[21:22]])
        nuc = EClass('nuclear',data_date='test')
        nuc_date_range = nuc._daterange(nuc.monthly_data,'197303','197401').Value.values
        assert np.array_equal(nuc_date_range,date_range)
    
    def test_daterange_BoundingDefaultDates(self,testdata):
        valarray = testdata.Value.values
        date_range = np.concatenate([valarray[8:20],valarray[21:23]])
        nuc = EClass('nuclear',data_date='test')
        nuc_date_range = nuc._daterange(nuc.monthly_data,None,None).Value.values
        assert np.array_equal(nuc_date_range,date_range)
      
    def test_totals_FindingMonthlyTotals(self,testdata):
        valarray = testdata.Value.values 
        monthly_totals = np.concatenate([valarray[8:20],valarray[21:23]])
        nuc = EClass('nuclear',data_date='test')
        nuc_monthly_totals = nuc.totals('monthly').Value.values
        assert np.array_equal(nuc_monthly_totals,monthly_totals)
        
    def test_totals_FindingYearlyTotals(self,testdata):
        valarray = testdata.Value.values 
        yearly_totals = np.array([valarray[7],valarray[20]])
        nuc = EClass('nuclear',data_date='test')
        nuc_yearly_totals = nuc.totals('yearly').Value.values
        assert np.array_equal(nuc_yearly_totals,yearly_totals)

    def test_totals_FindingCumulativeTotal(self,testdata):
        valarray = testdata.Value.values 
        cumulative_total = np.sum(np.array([valarray[7],valarray[20]]))
        nuc = EClass('nuclear',data_date='test')
        nuc_cumulative_total = nuc.totals('cumulative')
        assert nuc_cumulative_total == cumulative_total

    def test_extrema_FindingMaximumMonth(self,testdata):
        valarray = testdata.Value.values
        max_val = 0.20
        max_month = '197310'
        nuc = EClass('nuclear',data_date='test')
        nuc_max_val,nuc_max_month = nuc.extrema('max','monthly')
        assert nuc_max_val == max_val
        assert nuc_max_month == max_month

    def test_extrema_FindingMinimumMonth(self,testdata):
        valarray = testdata.Value.values
        min_val = 0.09
        min_month = '197303'
        nuc = EClass('nuclear',data_date='test')
        nuc_min_val,nuc_min_month = nuc.extrema('min','monthly')
        assert nuc_min_val == min_val
        assert nuc_min_month == min_month

    def test_extrema_FindingMaximumYear(self,testdata):
        valarray = testdata.Value.values
        max_val = 1.30
        max_year = '1973'
        nuc = EClass('nuclear',data_date='test')
        nuc_max_val,nuc_max_year = nuc.extrema('max','yearly')
        assert nuc_max_val == max_val
        assert nuc_max_year == max_year

    def test_extrema_FindingYearlyMinimum(self,testdata):
        valarray = testdata.Value.values
        min_val = 0.60
        min_year = '1972'
        nuc = EClass('nuclear',data_date='test')
        nuc_min_val,nuc_min_year = nuc.extrema('min','yearly')
        assert nuc_min_val == min_val
        assert nuc_min_year == min_year

