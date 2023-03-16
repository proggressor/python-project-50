import pytest
from gendiff.generate_diff import generate_diff


def test_wrong_extension():
    with pytest.raises(Exception):
        generate_diff('gendiff/parser.py', 'tests/fixtures/nested2.json')


@pytest.fixture
def expectation(style, hierarchy):
    path = f'tests/fixtures/expectations/{style}_{hierarchy}'
    with open(file=path) as file:
        diff = str.join('', file.readlines())
        return diff


@pytest.mark.parametrize(argvalues=['json', 'plain', 'stylish'],
                         argnames='style')
@pytest.mark.parametrize(argvalues=['flat'], argnames='hierarchy')
@pytest.mark.parametrize("path1,path2", [
    ('tests/fixtures/flat1.json', 'tests/fixtures/flat2.json'),
    ('tests/fixtures/flat1.yml', 'tests/fixtures/flat2.yml')
])
def test_gendiff_flat(path1, path2, style, expectation):
    assert generate_diff(path1, path2, output_format=style) == expectation


@pytest.mark.parametrize(argvalues=['json', 'plain', 'stylish'],
                         argnames='style')
@pytest.mark.parametrize(argvalues=['nested'], argnames='hierarchy')
@pytest.mark.parametrize("path1,path2", [
    ('tests/fixtures/nested1.json', 'tests/fixtures/nested2.json'),
    ('tests/fixtures/nested1.yml', 'tests/fixtures/nested2.yml')
])
def test_gendiff_nested(path1, path2, style, expectation):
    assert generate_diff(path1, path2, output_format=style) == expectation
