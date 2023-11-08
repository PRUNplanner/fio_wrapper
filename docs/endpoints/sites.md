# Sites
Exposes FIO Sites data for users, either as whole site data or warehouses. 
All Sites data requires a **FIO API KEY**. You will need to have access to the data the user has in FIO in order to access it.

## Example
```python
from fio_wrapper import FIO

fio = FIO(api_key="your_api_key")

# Get users warehouses
user_warehouses = fio.Sites.warehouses(username="PrUn username")

# Get users complete sites data incl. buildings, 
# their condition and repair / reclaimable materials
user_sites = fio.Sites.get(username="PrUn username")

# Get users sites data for specific planet incl. buildings, 
# their condition and repair / reclaimable materials
user_sites = fio.Sites.get_planet(username="PrUn username", planet="Montem")

```

## Endpoints

::: endpoints.endpoints_v1.sites