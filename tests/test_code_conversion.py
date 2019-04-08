import pytest
import pandas as pd
from pyleiades.utils.code_conversion import code_to_name as ctn
from pyleiades.utils.code_conversion import code_to_period as ctp
from pyleiades.utils.code_conversion import parse_input_date as parser

class TestCTN:

    def test_convert_name(self):
        assert ctn(1) == 'coal'

    def test_invalid_entry(self):
        with pytest.raises(KeyError):
            ctn('test')

class TestCTP:

    def test_yearly_code(self):
        assert ctp('202013') == pd.Period('2020', 'Y')

    def test_monthly_code(self):
        assert ctp('202001') == pd.Period('202001', 'M')

    def test_invalid_code(self):
        with pytest.raises(ValueError):
            ctp('test24')

class TestDateParser:

    def test_read_format_yyyy(self):
        assert parser('2017') == pd.Period('2017', 'Y')

    def test_read_format_yyyymm(self):
        assert parser('201708') == pd.Period('2017-08', 'M')

    def test_read_format_yyyy_mm(self):
        assert parser('2017-08') == pd.Period('2017-08', 'M')

    def test_read_format_mm_yyyy(self):
        assert parser('08-2017') == pd.Period('2017-08', 'M')

    def test_read_format_invalid_separator_position(self):
        with pytest.raises(ValueError):
            parser('8-22-17')

    def test_read_format_invalid_nonspecific_year(self):
        with pytest.raises(ValueError):
            parser('082-017')

    def test_read_format_invalid_nonspecific_date(self):
        with pytest.raises(ValueError):
            parser('17')

    def test_read_format_invalid_characters(self):
        with pytest.raises(ValueError):
            parser('1500ad')

    def test_read_format_invalid_year_early(self):
        with pytest.raises(ValueError):
            parser('1500')

    def test_read_format_invalid_year_late(self):
        with pytest.raises(ValueError):
            parser('5650')

    def test_read_format_invalid_month(self):
        with pytest.raises(ValueError):
            parser('200055')
