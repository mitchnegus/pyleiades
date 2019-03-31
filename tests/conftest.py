import pytest
import pyleiades
from pyleiades.utils.load_data import load_dataset

TEST_DATA_DIR = 'tests/test_data'
TEST_ARCHIVE_DIR = f'{TEST_DATA_DIR}/test_archive'

@pytest.fixture(scope="session")
def monkeysession():
    # This is required to use monkeypatch in the `module` scope
    #
    # NOTE: It relies on pytest's internal API and so therefore it  may not be
    #       supported in future releases
    #
    # See https://github.com/pytest-dev/pytest/issues/363 for more info
    from _pytest.monkeypatch import MonkeyPatch
    mpatch = MonkeyPatch()
    yield mpatch
    mpatch.undo()

@pytest.fixture(scope="session")
def testdata(monkeysession):
    monkeysession.setattr(pyleiades, 'DATA_DIR', TEST_DATA_DIR)
    monkeysession.setattr(pyleiades, 'ARCHIVE_DIR', TEST_ARCHIVE_DIR)
    return load_dataset()

@pytest.fixture(scope="module")
def testvals(testdata):
    return testdata.value.values
