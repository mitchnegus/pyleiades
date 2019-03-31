import pytest
from pyleiades.utils.load_data import load_dataset

@pytest.fixture(scope="module")
def testdata():
    return load_dataset(dataset_type='test')

@pytest.fixture(scope="module")
def testvals(testdata):
    return testdata.value.values
