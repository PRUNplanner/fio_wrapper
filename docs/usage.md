# Installation
```python
pip install fio-wrapper
```

# Usage
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
