import pytest
from . import test_results
from gendiff.generate_diff import generate_diff


@pytest.mark.parametrize("file_path1,file_path2,expected", [
    ('tests/fixtures/flat_test1.json', 'tests/fixtures/flat_test2.json',
     test_results.flat_stylish1),
    ('tests/fixtures/flat_test3.json', 'tests/fixtures/flat_test4.json',
     test_results.flat_stylish2),
    ('tests/fixtures/flat_test1.yml', 'tests/fixtures/flat_test2.yml',
     test_results.flat_stylish1),
    ('tests/fixtures/flat_test3.yml', 'tests/fixtures/flat_test4.yml',
     test_results.flat_stylish2)
])
def test_flat_stylish(file_path1, file_path2, expected):
    assert generate_diff(file_path1, file_path2) == expected


@pytest.mark.parametrize("file_path1,file_path2,expected", [
    ('tests/fixtures/nested_test1.json', 'tests/fixtures/nested_test2.json',
     test_results.nested_stylish1),
    ('tests/fixtures/nested_test1.yml', 'tests/fixtures/nested_test2.yml',
     test_results.nested_stylish1)
])
def test_nested_stylish(file_path1, file_path2, expected):
    assert generate_diff(file_path1, file_path2) == expected


@pytest.mark.parametrize("file_path1,file_path2,expected", [
    ('tests/fixtures/nested_test1.json', 'tests/fixtures/nested_test2.json',
     test_results.nested_plain1),
    ('tests/fixtures/nested_test1.yml', 'tests/fixtures/nested_test2.yml',
     test_results.nested_plain1)
])
def test_nested_plain(file_path1, file_path2, expected):
    assert generate_diff(file_path1, file_path2, output_format='plain') == expected
