import pytest
from pyleiades.utils.eia_codes import name_to_code as ntc
from pyleiades.utils.eia_codes import date_to_code as dtc

class TestNTC:

    def test_convert_name(self):
        assert ntc('coal') == 1

    def test_ignore_case(self):
        assert ntc('Renewable') == 11

    def test_invalid_entry(self):
        with pytest.raises(KeyError):
            ntc('test')

class TestDTC:

    def test_read_format_yyyy(self):
        assert dtc('2017') == '201701'

    def test_read_format_yyyymm(self):
        assert dtc('201708') == '201708'

    def test_read_format_yyyy_mm(self):
        assert dtc('2017-08') == '201708'

    def test_read_format_mm_yyyy(self):
        assert dtc('08-2017') == '201708'

    def test_read_format_invalid_separator_position(self):
        with pytest.raises(ValueError):
            dtc('8-22-17')

    def test_read_format_invalid_nonspecific_year(self):
        with pytest.raises(ValueError):
            dtc('082-017')

    def test_read_format_invalid_nonspecific_date(self):
        with pytest.raises(ValueError):
            dtc('17')

    def test_read_format_invalid_characters(self):
        with pytest.raises(ValueError):
            dtc('1500ad')

    def test_read_format_invalid_year_early(self):
        with pytest.raises(ValueError):
            dtc('1500')

    def test_read_format_invalid_year_late(self):
        with pytest.raises(ValueError):
            dtc('5650')

    def test_read_format_invalid_month(self):
        with pytest.raises(ValueError):
            dtc('200055')
