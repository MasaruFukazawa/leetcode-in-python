SRC_DIR = leetcode
TEST_DIR = tests
SERVICE = app
DC_RUN = docker compose run --rm $(SERVICE)

.PHONY: lint test prepare shell \
        lint-host test-host prepare-host \
        hooks-install hooks-run hooks-update \
        docker-build docker-up docker-down docker-restart \
        docker-logs docker-ps docker-clean

# ---- Default targets (run inside docker) ----

lint:
	$(DC_RUN) make lint-host

test:
	$(DC_RUN) make test-host

prepare:
	$(DC_RUN) make prepare-host

shell:
	docker compose exec $(SERVICE) bash

# ---- In-container implementations ----

lint-host:
	uv run ruff check --fix $(SRC_DIR) $(TEST_DIR)
	uv run ruff format $(SRC_DIR) $(TEST_DIR)
	uv run ty check $(SRC_DIR) $(TEST_DIR)

test-host:
	uv run pytest --cov=$(SRC_DIR) --cov-branch  --junitxml=pytest.xml --cov-report=term-missing:skip-covered | tee pytest-coverage.txt

prepare-host: lint-host test-host

# ---- pre-commit hooks ----

hooks-install:
	uv run pre-commit install

hooks-run:
	uv run pre-commit run --all-files

hooks-update:
	uv run pre-commit autoupdate

# ---- Docker container lifecycle ----

docker-build:
	docker compose build

docker-up:
	docker compose up -d

docker-down:
	docker compose down

docker-restart:
	docker compose restart

docker-logs:
	docker compose logs -f

docker-ps:
	docker compose ps

docker-clean:
	docker compose down --rmi local --volumes --remove-orphans
