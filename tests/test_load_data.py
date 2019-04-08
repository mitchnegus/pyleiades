import pytest
from pyleiades.utils import load_data

class TestLoadDataset:

    def test_load_dataset_default(self):
        test_df = load_data.load_dataset()
        assert len(test_df) == 23
        assert test_df.value.iloc[0] == 1.1
        assert list(test_df.columns) == ['date', 'value', 'energy_type']

    def test_load_dataset_specific_date(self):
        test_df = load_data.load_dataset(dataset_date='test')
        assert len(test_df) == 2
        assert test_df.value.iloc[0] == 7.5

    def test_load_dataset_specific_type(self):
        test_df = load_data.load_dataset(dataset_type='production')
        assert len(test_df) == 2
        assert test_df.value.iloc[0] == 2.5

    def test_load_dataset_invalid_date(self):
        with pytest.raises(ValueError):
            load_data.load_dataset(dataset_date='fail')

    def test_load_dataset_invalid_type(self):
        with pytest.raises(ValueError):
            load_data.load_dataset(dataset_type='fail')
