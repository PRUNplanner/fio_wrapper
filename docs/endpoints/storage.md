Exposes FIO Storage data for users.
All storage data requires a **FIO API KEY**. You will need to have access to the data the user has in FIO in order to access it.

Example:
```python
from fio_wrapper import FIO

fio = FIO(api_key="your_api_key")

# Get users storage data
user_storage = fio.Sites.get(username="PrUn username")
```

::: endpoints.endpoints_v1.storage