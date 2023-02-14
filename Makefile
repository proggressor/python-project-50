install: # развёртвыем poetry
	poetry install

build: check # сборка пакета
	poetry build

publish: # публикация пакета
	poetry publish --dry-run

package-install: # установка пакета из ОС
	python3 -m pip install --user dist/*.whl --force-reinstall

.PHONY: all gendiff clean

gendiff:
	poetry run gendiff

lint: # запуск линтера
	poetry run flake8 gendiff tests

test: # запуск тестов
	poetry run pytest
#	poetry run pytest --cov=gendiff --cov-report xml
#	poetry run pytest --cov-report term-missing --cov=gendiff
