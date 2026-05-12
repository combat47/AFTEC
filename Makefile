.PHONY: help install run-sim run-ingester test clean

help:
	@echo "Available commands:"
	@echo "  make install      - install dependencies"
	@echo "  make run-sim      - run mock sensor (generate fake data)"
	@echo "  make run-ingester - run main ingester (reads from mock or serial)"
	@echo "  make test         - run pytest"
	@echo "  make clean        - remove __pycache__ and .pytest_cache"

install:
	pip install -r requirements.txt
	pip install -e .   # install src/aftec in editable mode

run-sim:
	python scripts/run_mock_sensor.py

run-ingester:
	python scripts/run_ingester.py

test:
	pytest tests/ -v

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	rm -rf .pytest_cache
