install: # развёртвыем poetry
	poetry install

build: check # сборка пакета
	poetry build

publish: # публикация пакета
	poetry publish --dry-run

package-install: # установка пакета из ОС
	python3 -m pip install --user dist/*.whl --force-reinstall

lint: # запуск линтера
	poetry run flake8 gendiff tests

selfcheck:
	poetry check

check:
	make selfcheck test lint

test: # запуск тестов
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests

.PHONY: install test lint selfcheck check build