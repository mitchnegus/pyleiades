import numpy as np
from main.eclass import EClass


class TestEClass:
     
    def test_Preprocessing(self):
        testdata = np.array([[195001,1,5],
                             [195101,None,5],
                             [195201,1,5],
                             [195201,1,6]],
                           float)
        # eliminate nan, isolate energy, remove ecode column
        preprocdata = np.array([[195001,1],
                                [195201,1]],
                               float)
        EC = EClass('nuclear',testdata)
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
     
    def test_daterange_BoundingDates(self):
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
        assert np.array_equal(EC.daterange(195011,195102),boundedmonths)
      
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
