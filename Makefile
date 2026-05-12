.PHONY: help install dev-install run-sim run-ingester test lint format clean pre-commit

help:
	@echo "Available commands:"
	@echo "  make install       - install production dependencies"
	@echo "  make dev-install   - install all dependencies (including dev)"
	@echo "  make run-sim       - run mock sensor"
	@echo "  make run-ingester  - run main ingester"
	@echo "  make test          - run pytest"
	@echo "  make lint          - run flake8"
	@echo "  make format        - run black & isort"
	@echo "  make pre-commit    - install pre-commit hooks"
	@echo "  make clean         - remove cache files"

install:
	pip install -e .

dev-install:
	pip install -e .[dev]
	pre-commit install

run-sim:
	python -m aftec.scripts.run_mock_sensor

run-ingester:
	python -m aftec.scripts.run_ingester

test:
	pytest tests/ -v

lint:
	flake8 src/ tests/

format:
	black src/ tests/
	isort src/ tests/

pre-commit:
	pre-commit run --all-files

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .coverage coverage.xml
