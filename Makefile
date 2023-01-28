install: #развёртвыем poetry
	poetry install

gendiff: #запуск brain-games
	poetry run gendiff

build: #сборка пакета
	poetry build

publish: #публикация пакета
	poetry publish --dry-run

package-install: #установка пакета из ОС
	python3 -m pip install --user dist/*.whl --force-reinstall
	
lint: #запуск линтера
	poetry run flake8 gendiff
	