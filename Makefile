build:
	uv build

install:
	uv sync

package-install:
	uv tool install dist/*.whl

package-install-force:
	uv tool install --force dist/*.whl

build-package: build package-install-force

lint:
	uv run ruff check brain_games

brain-games:
	uv run brain-games