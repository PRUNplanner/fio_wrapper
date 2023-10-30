# pyfio

Python API wrapper for Prosperous Universes community API FIO.

# Usage

```python
from pyfio.fio import FIO

fio = FIO()

material = fio.Material.get("DW")
print(Material.Ticker)
```
> DW

# Tests

**pyfio** uses pytest, requests_mock and pytest-cov to run tests, mock calls towards FIO endpoints and generate the code coverage report.

Run tests:
```shell
pytest 
```

Generate coverage report:
```shell
pytest --cov --cov-report=html:coverage --cov-config=.coveragerc
```
