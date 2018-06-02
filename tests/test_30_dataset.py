
import os.path

import pytest

from eccodes_grib import dataset

SAMPLE_DATA_FOLDER = os.path.join(os.path.dirname(__file__), 'sample-data')
TEST_DATA = os.path.join(SAMPLE_DATA_FOLDER, 'era5-levels-members-one_var.grib')


def test_dict_merge():
    master = {'one': 1}
    dataset.dict_merge(master, {'two': 2})
    assert master == {'one': 1, 'two': 2}
    dataset.dict_merge(master, {'two': 2})
    assert master == {'one': 1, 'two': 2}

    with pytest.raises(ValueError):
        dataset.dict_merge(master, {'two': 3})


def test_Dataset():
    dataset.Dataset.fromstream(TEST_DATA)


def test_DataVariable():
    res = dataset.DataVariable.fromstream(path=TEST_DATA, paramId=130, name='tas')
    assert res.name == 'tas'
