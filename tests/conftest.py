import pytest
from pyleiades.utils.load_data import load_dataset

@pytest.fixture(scope="module")
def testdata():
    return load_dataset('test')
