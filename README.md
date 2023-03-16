### Hexlet tests, linter and CI status:
[![Actions Status](https://github.com/proggressor/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/proggressor/python-project-50/actions)
[![Python CI](https://github.com/proggressor/python-project-50/actions/workflows/tests.yml/badge.svg)](https://github.com/proggressor/python-project-50/actions/workflows/tests.yml)

### Codeclimat: Maintainability and Code coverage
[![Maintainability](https://api.codeclimate.com/v1/badges/24650d708145428abe17/maintainability)](https://codeclimate.com/github/proggressor/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/24650d708145428abe17/test_coverage)](https://codeclimate.com/github/proggressor/python-project-50/test_coverage)



### Minimum requirements for installed packages
Python, version 3.10
Poetry, version 1.2.2

### Project Description
This is my second study project at the Hexlet programming school.
It's a simple calculator of the differences between two *json* or *yaml* files.

### Package installation procedure
1. `make install` # poetry install
2. `make build` # poetry build
3. `make package-install` # python3 -m pip install --user dist/*.whl --force-reinstall

### Examples of how the utility works

1. Simple flat **json** files with *stylish* (default) output format: 
`gendiff tests/fixtures/flat1.json tests/fixtures/flat2.json`
[![asciicast](https://asciinema.org/a/dzajPelmD79JMVfiqz9m1aoGR.svg)](https://asciinema.org/a/dzajPelmD79JMVfiqz9m1aoGR)

2. Simple flat **yml** files with *stylish* (default) output format: 
`gendiff tests/fixtures/flat1.yml tests/fixtures/flat2.yml`
[![asciicast](https://asciinema.org/a/G9uXhg0hGd5DwfqBKRSHHyR9I.svg)](https://asciinema.org/a/G9uXhg0hGd5DwfqBKRSHHyR9I)

3. Nested **json** files with *stylish* (default) output format: 
`gendiff tests/fixtures/nested1.json tests/fixtures/nested2.json`
[![asciicast](https://asciinema.org/a/YdXjInqqgMHlhmsQaB82hwXlN.svg)](https://asciinema.org/a/YdXjInqqgMHlhmsQaB82hwXlN)

4. Nested **json** files with *plain* output format: 
`gendiff -f plain tests/fixtures/nested1.json tests/fixtures/nested2.json`
[![asciicast](https://asciinema.org/a/98jxWIkEn3FFZzGgGhfqJHsca.svg)](https://asciinema.org/a/98jxWIkEn3FFZzGgGhfqJHsca)

5. Nested **json** files with *json* output format: 
`gendiff -f json tests/fixtures/nested1.json tests/fixtures/nested2.json`
[![asciicast](https://asciinema.org/a/56NlrihdYZt3kt19qHtscI0JX.svg)](https://asciinema.org/a/56NlrihdYZt3kt19qHtscI0JX)