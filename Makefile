install: # развёртвыем poetry
	poetry install

build: # сборка пакета
	poetry build

publish: # публикация пакета
	poetry publish --dry-run

package-install: # установка пакета из ОС
	python3 -m pip install --user dist/*.whl --force-reinstall

gendiff:
	poetry run gendiff -h

lint: # запуск линтера
	poetry run flake8 gendiff tests

test: # запуск тестов
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests