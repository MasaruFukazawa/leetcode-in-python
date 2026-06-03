SRC_DIR = leetcode
TEST_DIR = tests
SERVICE = app

.PHONY: lint test prepare shell \
        docker-build docker-up docker-down docker-restart \
        docker-shell docker-logs docker-ps docker-clean \
        docker-lint docker-test docker-prepare

lint:
	uv run ruff check --fix $(SRC_DIR) $(TEST_DIR)
	uv run ruff format $(SRC_DIR) $(TEST_DIR)
	uv run ty check $(SRC_DIR) $(TEST_DIR)

test:
	uv run pytest --cov=$(SRC_DIR) --cov-branch  --junitxml=pytest.xml --cov-report=term-missing:skip-covered | tee pytest-coverage.txt

prepare:
	make lint
	make test

# ---- Docker operations ----

docker-build:
	docker compose build

docker-up:
	docker compose up -d

docker-down:
	docker compose down

docker-restart:
	docker compose restart

docker-shell shell:
	docker compose exec $(SERVICE) bash

docker-logs:
	docker compose logs -f

docker-ps:
	docker compose ps

docker-clean:
	docker compose down --rmi local --volumes --remove-orphans

docker-lint:
	docker compose run --rm $(SERVICE) make lint

docker-test:
	docker compose run --rm $(SERVICE) make test

docker-prepare:
	docker compose run --rm $(SERVICE) make prepare
