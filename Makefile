build:
	uv build

install:
	uv sync

package-install:
	uv tool install dist/*.whl

package-install-force:
	uv tool install --force dist/*.whl

package-update: build package-install-force

lint:
	uv run ruff check brain_games

lint-fix:
	uv run ruff check brain_games --fix

brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

brain-gcd:
	uv run brain-gcd

brain-progression:
	uv run brain-progression

brain-prime:
	uv run brain-prime
