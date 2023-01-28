install: #развёртвыем poetry
	poetry install

gendiff_help: #запуск мануала по gendiff
	poetry run gendiff -h

build: #сборка пакета
	poetry build

publish: #публикация пакета
	poetry publish --dry-run

package-install: #установка пакета из ОС
	python3 -m pip install --user dist/*.whl --force-reinstall
	
lint: #запуск линтера
	poetry run flake8 gendiff
	