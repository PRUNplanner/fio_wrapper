# Usage
## Installation
```python
pip install fio-wrapper
```

## Simple Usage
Creating the FIO adapter and looking for information about the material Drinking Water by its ticker "DW".
```python
from fio_wrapper import FIO

fio = FIO()

material = fio.Material.get("DW")

print(material.model_dump_json())
```

This will print the material information of Drinking Water as MaterialModel and it's JSON.

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

## Additional parameters

FIO Wrapper allows you to specify additional attributes when instantiating. The most commonly used is `api_key` that lets you add your FIO API Key (obtained on the [FIO Website](https://fio.fnar.net/settings)) to access protected endpoints like [Site](endpoints/sites.md) or [Storage](endpoints/storage.md).

```python
from fio_wrapper import FIO

fio = FIO(api_key="YOUR_FIO_API_KEY")
```

The complete list of parameters can be found on [`FIO()`](fio.md).

## Configuration file

FIO Wrapper can use a configuration file provided upon instantiation to overwrite its [base configuration](config.md).

Example configuration file `config.yml`:

```yaml
fio:
  application: MyExampleApplication
  version: 1.0.0
cache:
  enabled: true
  default_expire: 10 # seconds
  urls:
    "*/material/*": 3600
    "*/exchange/all": NEVER_EXPIRE
    "*/exchange/full": DO_NOT_CACHE
```

Use this configuration file on [`FIO()`](fio.md) by providing the `config` attribute:

```python
from fio_wrapper import FIO

fio = FIO(config="config.yml")
```