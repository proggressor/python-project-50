import pytest
from os.path import join as opj
from . import test_results
from gendiff.generate_diff import generate_diff


full_path = '/home/proggressor/python-project-50/tests/fixtures'


@pytest.mark.parametrize("file_path1,file_path2,expected", [
    (opj(full_path, 'test_file1.json'), opj(full_path, 'test_file2.json'),
     test_results.flat_file1),
    (opj(full_path, 'test_file3.json'), opj(full_path, 'test_file4.json'),
     test_results.flat_file2),
])
def test_json(file_path1, file_path2, expected):
    assert generate_diff(file_path1, file_path2) == expected


@pytest.mark.parametrize("file_path1,file_path2,expected", [
    (opj(full_path, 'test_file1.yml'), opj(full_path, 'test_file2.yml'),
     test_results.flat_file1),
    (opj(full_path, 'test_file3.yml'), opj(full_path, 'test_file4.yml'),
     test_results.flat_file2)
])
def test_yaml(file_path1, file_path2, expected):
    assert generate_diff(file_path1, file_path2) == expected
