build:
	uv build

install:
	uv sync

package-install:
	uv tool install dist/*.whl

package-install-force:
	uv tool install --force dist/*.whl

brain-games:
	uv run brain-games