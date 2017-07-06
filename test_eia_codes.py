from energy_codes import name_to_code as ntc


class TestNTC:
    
    def test_ntc_code():
        assert ntc('coal') == 1
    
    def test_ntc_case():
        assert ntc('Renewable') == 11
