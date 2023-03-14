import pytest
from . import expectations
from gendiff.generate_diff import generate_diff


@pytest.mark.parametrize("file_path1,file_path2,expected", [
    ('tests/fixtures/flat_test1.json', 'tests/fixtures/flat_test2.json',
     expectations.flat_stylish1),
    ('tests/fixtures/flat_test1.yml', 'tests/fixtures/flat_test2.yml',
     expectations.flat_stylish1),
    ('tests/fixtures/flat_test3.json', 'tests/fixtures/flat_test4.json',
     expectations.flat_stylish2),
    ('tests/fixtures/flat_test3.yml', 'tests/fixtures/flat_test4.yml',
     expectations.flat_stylish2)
])
def test_flat_stylish(file_path1, file_path2, expected):
    assert generate_diff(file_path1, file_path2) == expected


@pytest.mark.parametrize("file_path1,file_path2,expected", [
    ('tests/fixtures/nested_test1.json', 'tests/fixtures/nested_test2.json',
     expectations.nested_stylish1),
    ('tests/fixtures/nested_test1.yml', 'tests/fixtures/nested_test2.yml',
     expectations.nested_stylish1),
    ('tests/fixtures/nested_test3.json', 'tests/fixtures/nested_test4.json',
     expectations.nested_stylish2),
    ('tests/fixtures/nested_test3.yml', 'tests/fixtures/nested_test4.yml',
     expectations.nested_stylish2)
])
def test_nested_stylish(file_path1, file_path2, expected):
    assert generate_diff(file_path1, file_path2) == expected


@pytest.mark.parametrize("file_path1,file_path2,expected", [
    ('tests/fixtures/flat_test1.json', 'tests/fixtures/flat_test2.json',
     expectations.flat_plain1),
    ('tests/fixtures/flat_test1.yml', 'tests/fixtures/flat_test2.yml',
     expectations.flat_plain1),
    ('tests/fixtures/flat_test3.json', 'tests/fixtures/flat_test4.json',
     expectations.flat_plain2),
    ('tests/fixtures/flat_test3.yml', 'tests/fixtures/flat_test4.yml',
     expectations.flat_plain2)
])
def test_flat_plain(file_path1, file_path2, expected):
    assert generate_diff(file_path1, file_path2,
                         output_format='plain') == expected


@pytest.mark.parametrize("file_path1,file_path2,expected", [
    ('tests/fixtures/nested_test1.json', 'tests/fixtures/nested_test2.json',
     expectations.nested_plain1),
    ('tests/fixtures/nested_test1.yml', 'tests/fixtures/nested_test2.yml',
     expectations.nested_plain1),
    ('tests/fixtures/nested_test3.json', 'tests/fixtures/nested_test4.json',
     expectations.nested_plain2),
    ('tests/fixtures/nested_test3.yml', 'tests/fixtures/nested_test4.yml',
     expectations.nested_plain2)
])
def test_nested_plain(file_path1, file_path2, expected):
    assert generate_diff(file_path1, file_path2,
                         output_format='plain') == expected


@pytest.mark.parametrize("file_path1,file_path2,expected", [
    ('tests/fixtures/flat_test1.json', 'tests/fixtures/flat_test2.json',
     expectations.flat_json1),
    ('tests/fixtures/flat_test1.yml', 'tests/fixtures/flat_test2.yml',
     expectations.flat_json1),
    ('tests/fixtures/flat_test3.json', 'tests/fixtures/flat_test4.json',
     expectations.flat_json2),
    ('tests/fixtures/flat_test3.yml', 'tests/fixtures/flat_test4.yml',
     expectations.flat_json2)
])
def test_flat_json(file_path1, file_path2, expected):
    assert generate_diff(file_path1, file_path2) == expected


def test_wrong_extension():
    with pytest.raises(Exception):
        generate_diff('gendiff/parser.py', 'tests/fixtures/nested_test2.json')
