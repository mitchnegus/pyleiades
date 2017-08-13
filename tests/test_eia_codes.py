from utils.eia_codes import name_to_code as ntc
from utils.eia_codes import date_to_code as dtc


class TestNTC:
    
    def test_ntc_ConvertingName(self):
        assert ntc('coal') == 1
    
    def test_ntc_IgnoringCase(self):
        assert ntc('Renewable') == 11

class TestDTC:

    def test_dtc_ReadingFormat1(self):
        assert dtc('201708') == float(201708)

    def test_dtc_ReadingFormat2(self):
        assert dtc('2017-08') == float(201708)
        
    def test_dtc_ReadingFormat3(self):
        assert dtc('08-2017') == float(201708)

    def test_dtc_ReadingFormat4(self):
        assert dtc('08/2017') == float(201708)

