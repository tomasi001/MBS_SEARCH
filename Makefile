.PHONY: help install test lint format check clean coverage docs

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	poetry install

test: ## Run tests
	poetry run pytest

test-cov: ## Run tests with coverage
	poetry run pytest --cov=src --cov-report=html --cov-report=term-missing

lint: ## Run linting
	poetry run ruff check src tests
	poetry run black --check src tests

format: ## Format code
	poetry run black src tests
	poetry run ruff check --fix src tests

check: lint test ## Run linting and tests

clean: ## Clean up generated files
	rm -rf .coverage htmlcov/ .pytest_cache/ .ruff_cache/ dist/ build/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

coverage: test-cov ## Generate coverage report
	@echo "Coverage report generated in htmlcov/index.html"

ci: check ## CI pipeline (lint + test)
	@echo "CI pipeline completed successfully"

load-sample: ## Load sample data for testing
	poetry run mbs-load --csv data/sample.csv

load-full: ## Load full XML data (requires MBS_XML_PATH env var)
	@if [ -z "$$MBS_XML_PATH" ]; then \
		echo "Error: MBS_XML_PATH environment variable not set"; \
		echo "Usage: MBS_XML_PATH=/path/to/mbs.xml make load-full"; \
		exit 1; \
	fi
	poetry run mbs-load --xml $$MBS_XML_PATH

analyze-xml: ## Analyze XML structure (requires MBS_XML_PATH env var)
	@if [ -z "$$MBS_XML_PATH" ]; then \
		echo "Error: MBS_XML_PATH environment variable not set"; \
		echo "Usage: MBS_XML_PATH=/path/to/mbs.xml make analyze-xml"; \
		exit 1; \
	fi
	poetry run mbs analyze-xml $$MBS_XML_PATH

serve: ## Start the development server
	poetry run uvicorn api.main:app --host 127.0.0.1 --port 8000 --reload

dev-setup: install load-sample ## Set up development environment
	@echo "Development environment ready!"
	@echo "Run 'make serve' to start the server"
