

.PHONY: install
install:
	poetry install

.PHONY: build
build: install
	poetry build

.PHONY: black
black: install
	poetry run black .

.PHONY: pytest
pytest: install
	poetry run pytest