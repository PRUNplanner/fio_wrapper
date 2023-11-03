# *fio_wrapper* - Prosperous Universe game data through FIO

[![PyPI - Version](https://img.shields.io/pypi/v/fio-wrapper.svg)](https://pypi.org/project/fio-wrapper)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fio-wrapper.svg)](https://pypi.org/project/fio-wrapper)
[![License: MIT](https://img.shields.io/badge/license-MIT-C06524)](https://github.com/jplacht/fio_wrapper/blob/master/LICENSE.md)
![PyPI - Downloads](https://img.shields.io/pypi/dm/fio-wrapper)

---

[FIO](https://doc.fnar.net/) API wrapper with [pydantic](https://github.com/pydantic/pydantic) data validation and easy-to-use querying. **fio_wrapper** implements the most used endpoints of Prosperous Universes community game data API.

- Source Code: [https://github.com/jplacht/fio_wrapper](https://github.com/jplacht/fio_wrapper)
- Documentation: [https://jplacht.github.io/fio_wrapper/](https://jplacht.github.io/fio_wrapper/)
- PyPi Package: [https://pypi.org/project/fio-wrapper/](https://pypi.org/project/fio-wrapper/)

# Usage
## Installation
```python
pip install fio-wrapper
```

## Access data
Creating the FIO adapter and looking for information about the material Drinking Water by its ticker "DW".
```python
from fio_wrapper import FIO

fio = FIO()

material = fio.Material.get("DW")
print(material)
print(material.model_dump_json())
```

This will print the material information of Drinking Water as MaterialModel and it's JSON.
```python
MaterialId='4fca6f5b5e6c3b8a1b887c6dc99db146' CategoryName='consumables (basic)' CategoryId='3f047ec3043bdd795fd7272d6be98799' Name='drinkingWater' Ticker='DW' Weight=0.10000000149011612 Volume=0.10000000149011612 UserNameSubmitted='SAGANAKI' Timestamp=datetime.datetime(2023, 10, 28, 19, 26, 21, 831707)
```

```json
{
    "MaterialId": "4fca6f5b5e6c3b8a1b887c6dc99db146",
    "CategoryName": "consumables (basic)",
    "CategoryId": "3f047ec3043bdd795fd7272d6be98799",
    "Name": "drinkingWater",
    "Ticker": "DW",
    "Weight": 0.10000000149011612,
    "Volume": 0.10000000149011612,
    "UserNameSubmitted": "SAGANAKI",
    "Timestamp": "2023-10-28T19:26:21.831707"
}
```

# Contributing

We welcome contributions of all types! In order to set up **fio_wrapper** locally please do the following:

1. Install Python + Poetry
2. Run the poetry environment and install depenencies
3. We are aiming for 100% code coverage

# Tests

**fio_wrapper** uses `pytest`, `requests_mock` and `pytest-cov` to run tests, mock calls towards FIO endpoints and generate the code coverage report and use `black` as formatter.

Run tests:
```shell
pytest 
```

Generate coverage report:
```shell
pytest --cov --cov-report=html:coverage --cov-config=.coveragerc
```

# Documentation

```shell
mkdocs gh-deploy 
```