import pandas as pd
import numpy as np
from main.eclass import EClass


class TestEClass:
     
    def test_MonthlyData(self):
        monthlydata = pd.DataFrame({'Date':'197301','Value':0.1},
                                   {'Date':'197302','Value':0.1},
                                   {'Date':'197303','Value':0.1},
                                   {'Date':'197304','Value':0.1},
                                   {'Date':'197305','Value':0.1},
                                   {'Date':'197306','Value':0.1},
                                   {'Date':'197307','Value':0.1},
                                   {'Date':'197308','Value':0.1},
                                   {'Date':'197309','Value':0.1},
                                   {'Date':'197310','Value':0.2},
                                   {'Date':'197311','Value':0.1},
                                   {'Date':'197312','Value':0.1},)
        monthlydata = monthlydata.set_index('Date_code')
        EC = EClass('nuclear',data_date='test')
        assert np.array_equal(EC.data,preprocdata)

    def test_FindingInitialDate(self):
        testdata = np.array([[195001,1,5],
                             [195101,1,5]],
                            float)
        EC = EClass('nuclear',testdata)
        assert EC.idate == 195001
    
    def test_FindingFinalDate(self):
        testdata = np.array([[195001,1,5],
                             [195101,1,5]],
                            float)
        EC = EClass('nuclear',testdata)
        assert EC.fdate == 195101
     
    def test_daterange_BoundingInputDates(self):
        testdata = np.array([[195010,1,5],
                             [195011,2,5],
                             [195012,2,5],
                             [195013,7,5],
                             [195101,2,5],
                             [195102,1,5],
                             [195103,1,5]],
                            float)
        boundedmonths = np.array([[195011,2],
                                  [195012,2],
                                  [195013,7],
                                  [195101,2],
                                  [195102,1]],
                                 float)
        EC = EClass('nuclear',testdata)
        assert np.array_equal(EC._daterange(195011,195102),boundedmonths)
    
    def test_daterange_BoundingDefaultDates(self):
        testdata = np.array([[195010,1,5],
                             [195011,2,5],
                             [195012,2,5],
                             [195013,7,5],
                             [195101,2,5],
                             [195102,1,5],
                             [195103,1,5]],
                            float)
        EC = EClass('nuclear',testdata)
        assert np.array_equal(EC._daterange(None,None),testdata[:,0:2])
      
    def test_monthlydata_FindingDataByMonth(self):
        testdata = np.array([[195013,2,5],
                             [195101,1,5],
                             [195102,1,5],
                             [195113,3,5]],
                            float)
        monthlydata = np.array([[195101,1],
                                  [195102,1]],
                                 float)
        EC = EClass('nuclear',testdata)
        testdata_bounded = EC._daterange(None,None)
        assert np.array_equal(EC._monthlydata(testdata_bounded),monthlydata)
        
    def test_yearlydata_FindingDataByYear(self):
        testdata = np.array([[195013,2,5],
                             [195101,1,5],
                             [195102,1,5],
                             [195113,3,5]],
                            float)
        yearlydata = np.array([[195013,2],
                                 [195113,3]],
                                float)
        EC = EClass('nuclear',testdata)
        testdata_bounded = EC._daterange(None,None)
        assert np.array_equal(EC._yearlydata(testdata_bounded),yearlydata)
        
    def test_totals_FindingMonthlyTotals(self):
        testdata = np.array([[195013,2,5],
                             [195101,1,5],
                             [195102,1,5],
                             [195113,3,5]],
                            float)
        monthlytotals = np.array([[195101,1],
                                  [195102,1]],
                                 float)
        EC = EClass('nuclear',testdata)
        assert np.array_equal(EC.totals(freq='monthly'),monthlytotals)
        
    def test_totals_FindingYearlyTotals(self):
        testdata = np.array([[195013,2,5],
                             [195101,1,5],
                             [195102,1,5],
                             [195113,3,5]],
                            float)
        yearlytotals = np.array([[195013,2],
                                 [195113,3]],
                                float)
        EC = EClass('nuclear',testdata)
        assert np.array_equal(EC.totals(freq='yearly'),yearlytotals)

    def test_totals_FindingCumulativeTotal(self):
        testdata = np.array([[195013,2,5],
                             [195101,1,5],
                             [195113,3,5],
                             [195201,1,5]],
                            float)
        cumulativetotal = np.array([[195201,6]],
                                   float)
        EC = EClass('nuclear',testdata)
        assert np.array_equal(EC.totals(freq='cumulative'),cumulativetotal)

    def test_extrema_FindingMonthlyMaximum(self):
        testdata = np.array([[195013,6,5],
                             [195101,1,5],
                             [195102,4,5],
                             [195113,5,5],
                             [195201,1,5]],
                            float)
        monthlymax = np.array([[195102,4]],
                              float)
        EC = EClass('nuclear',testdata)
        assert np.array_equal(EC.extrema('max','monthly'),monthlymax)

    def test_extrema_FindingMonthlyMinimum(self):
        testdata = np.array([[195013,6,5],
                             [195101,1,5],
                             [195102,4,5],
                             [195113,5,5],
                             [195201,2,5]],
                            float)
        monthlymin = np.array([[195101,1]],
                              float)
        EC = EClass('nuclear',testdata)
        assert np.array_equal(EC.extrema('min','monthly'),monthlymin)

    def test_extrema_FindingYearlyMinimum(self):
        testdata = np.array([[195013,7,5],
                             [195101,2,5],
                             [195102,3,5],
                             [195113,5,5],
                             [195201,1,5]],
                            float)
        yearlymin = np.array([[195113,5]],
                              float)
        EC = EClass('nuclear',testdata)
        assert np.array_equal(EC.extrema('min','yearly'),yearlymin)

    def test_extrema_FindingYearlyMaximum(self):
        testdata = np.array([[195013,4,5],
                             [195101,2,5],
                             [195102,3,5],
                             [195113,5,5],
                             [195201,1,5]],
                            float)
        yearlymax = np.array([[195113,5]],
                              float)
        EC = EClass('nuclear',testdata)
        assert np.array_equal(EC.extrema('max','yearly'),yearlymax)


