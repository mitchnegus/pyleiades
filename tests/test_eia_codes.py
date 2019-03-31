from pyleiades.utils.eia_codes import name_to_code as ntc
from pyleiades.utils.eia_codes import date_to_code as dtc

class TestNTC:

    def test_convert_name(self):
        assert ntc('coal') == 1

    def test_ignore_case(self):
        assert ntc('Renewable') == 11

class TestDTC:

    def test_read_format_yyyy(self):
        assert dtc('2017') == '201701'

    def test_read_format_yyyymm(self):
        assert dtc('201708') == '201708'

    def test_read_format_yyyy_mm(self):
        assert dtc('2017-08') == '201708'

    def test_read_format_mm_yyyy(self):
        assert dtc('08-2017') == '201708'
