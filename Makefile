install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall  dist/*.whl

lint:
	poetry run flake8 .

setup: install build publish package-install
check: build publish package-install