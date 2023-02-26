import pytest
from . import test_results
from gendiff.generate_diff import generate_diff


@pytest.mark.parametrize("file_path1,file_path2,expected", [
    ('tests/fixtures/flat_test1.json', 'tests/fixtures/flat_test2.json',
     test_results.flat_file1),
    ('tests/fixtures/flat_test3.json', 'tests/fixtures/flat_test4.json',
     test_results.flat_file2),
])
def test_flat_json(file_path1, file_path2, expected):
    assert generate_diff(file_path1, file_path2) == expected


@pytest.mark.parametrize("file_path1,file_path2,expected", [
    ('tests/fixtures/flat_test1.yml', 'tests/fixtures/flat_test2.yml',
     test_results.flat_file1),
    ('tests/fixtures/flat_test3.yml', 'tests/fixtures/flat_test4.yml',
     test_results.flat_file2)
])
def test_flat_yml(file_path1, file_path2, expected):
    assert generate_diff(file_path1, file_path2) == expected


@pytest.mark.parametrize("file_path1,file_path2,expected", [
    ('tests/fixtures/nested_test1.json', 'tests/fixtures/nested_test2.json',
     test_results.nested_file1),
])
def test_nest_json(file_path1, file_path2, expected):
    assert generate_diff(file_path1, file_path2) == expected


@pytest.mark.parametrize("file_path1,file_path2,expected", [
    ('tests/fixtures/nested_test1.yml', 'tests/fixtures/nested_test2.yml',
     test_results.nested_file1),
])
def test_nest_yml(file_path1, file_path2, expected):
    assert generate_diff(file_path1, file_path2) == expected
