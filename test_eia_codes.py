from eia_codes import name_to_code as ntc


class TestNTC:
    
    def test_ntc_code(self):
        assert ntc('coal') == 1
    
    def test_ntc_case(self):
        assert ntc('Renewable') == 11
