install:
	uv sync


gendiff:
	uv run gendiff


build:
	uv build


package-install:
	uv tool install --force dist/hexlet_code-0.1.0-py3-none-any.whl


lint:
	ruff check


test:
	pytest