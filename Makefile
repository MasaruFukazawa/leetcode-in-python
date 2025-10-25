SRC_DIR = leetcode
TEST_DIR = tests

lint:
	uv run flake8 --ignore=E265,E501,E741 $(SRC_DIR)
	uv run flake8 --ignore=E265,E501,E741 $(TEST_DIR)
	uv run black $(SRC_DIR)
	uv run black $(TEST_DIR)
	uv run isort $(SRC_DIR)
	uv run isort $(TEST_DIR)
	uv run mypy --check-untyped-defs $(SRC_DIR)
	uv run mypy --check-untyped-defs $(TEST_DIR)
	uv run bandit -r $(SRC_DIR)

test:
	uv run pytest --cov=$(SRC_DIR) --cov-branch  --junitxml=pytest.xml --cov-report=term-missing:skip-covered | tee pytest-coverage.txt

prepare:
	make lint
	make test
