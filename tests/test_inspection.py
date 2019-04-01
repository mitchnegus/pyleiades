import pytest
from pyleiades.utils.inspection import check_if_method

@pytest.fixture
def sample_class_instance():
    class X:
        not_a_method = None
        def method(self):
            pass
    return X()

class TestInspection:

    def test_check_if_method_true(self, sample_class_instance):
        assert check_if_method(sample_class_instance, 'method')

    def test_check_if_method_false(self):
        assert not check_if_method(sample_class_instance, 'not_a_method')

    def test_check_if_method_missing(self):
        assert not check_if_method(sample_class_instance, 'test')
