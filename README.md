# AIOps CI Challenge

This project contains a small Python service telemetry utility and a GitHub Actions CI setup for automated testing and coverage reporting.

## Project overview

The repository includes:
- utility functions for calculating circle area and Fibonacci numbers in [src/calculations.py](src/calculations.py)
- anomaly detection and event-processing logic in [src](src)
- automated tests in [tests](tests)
- GitHub Actions workflows in [.github/workflows](.github/workflows)

## Local setup

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install pytest pytest-cov
```

## Run tests locally

```bash
PYTHONPATH=. pytest -ra --cov=src --cov-report=term-missing --cov-fail-under=50
```

## GitHub Actions

The repository includes pull-request workflows for:
- automated test execution
- coverage generation and coverage threshold enforcement

These workflows are defined in [.github/workflows/test.yml](.github/workflows/test.yml) and [.github/workflows/python-coverage.yml](.github/workflows/python-coverage.yml).

---

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)

