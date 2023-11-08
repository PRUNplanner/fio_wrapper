# Setting up

- Git clone this project on your local machine
- Install poetry (`pip install poetry`)
- Install dependencies
  - `poetry install`
  - For documentation changes, run `poetry install --with docs`

It is recommended to have Poetry create `.venv` folder by setting this as config, see: [Poetry Local Configuration](https://python-poetry.org/docs/configuration/#local-configuration) and set up your IDE (e.g. VSCode) to use this environment for all development.

# Running tests

All tests make use of `pytest` with `requests_mock`, coverage reports are made with `pytest-cov`.

Run all tests with: `pytest` in your Poetry environment.

Coverage report generation uses `.coveragerc` configuration file, run the coverage report creation with: `pytest --cov --cov-report=html:coverage --cov-config=.coveragerc`

# Running mkdocs locally

Use `mkdocs serve` to run documentation locally after you installed the dependencies (see "Setting Up")

# Versioning

Versioning is handled via Github Tags upon Release creation and not from within `pyproject.toml`.


# Pull Requests

We are very happy to receive Pull Requests and help to move FIO Wrapper forward, please ensure the following before creating a PR:

1. Formatting with `black` is ensured
2. All additions are covered with tests
3. All tests run succesfully locally using `pytest`
4. Test Coverage is at 100%
