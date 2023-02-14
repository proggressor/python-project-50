import pytest
from . import test_results
from gendiff.generate_diff import generate_diff


@pytest.mark.parametrize("file_path1,file_path2,expected", [
    ('tests/fixtures/test_file1.json', 'tests/fixtures/test_file2.json',
     test_results.flat_json1),
    ('tests/fixtures/test_file3.json', 'tests/fixtures/test_file4.json',
     test_results.flat_json2)
])
def test_json(file_path1, file_path2, expected):
    assert generate_diff(file_path1, file_path2) == expected
