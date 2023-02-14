install: # развёртвыем poetry
	poetry install

gendiff: # запуск мануала по gendiff
	poetry run gendiff -h

build: check # сборка пакета
	poetry build

publish: # публикация пакета
	poetry publish --dry-run

package-install: # установка пакета из ОС
	python3 -m pip install --user dist/*.whl --force-reinstall
	
lint: # запуск линтера
	poetry run flake8 gendiff

test: # запуск текстов
	poetry run pytest
	poetry run pytest --cov=gendiff --cov-report xml
	poetry run pytest --cov-report term-missing --cov=gendiff

.PHONY: all gendiff clean
