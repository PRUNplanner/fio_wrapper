# Timeouts 
## Logic
All calls the wrapper makes towards FIO contain a specified timeout value on [`requests`](https://requests.readthedocs.io/en/latest/user/advanced/#timeouts) to not keep your program in an infinite loop.

Timeouts can be defined by the user on two levels:

1. Upon instantiation of the `FIO` class
2. Upon individual endpoint calls

FIO Wrapper includes a default fallback to `10.0` seconds, if no value is defined by the user. Overwriting to `None` to disable timeouts is possible.

## [`FIO`](fio.md) instantiation

Define a default timeout for all requests by overwriting the [`Adapter`](fio_adapter.md) default.

```python
from fio_wrapper import FIO

# set timeout to 5 seconds
fio = FIO(timeout=5)

```

FIO Wrapper will now apply the timeout of `5 seconds` to all calls it is making towards FIO.

## Indidivual endpoint calls

All endpoints allow passing the optional `timeout` argument that is of type `Optional[float]` and defaults to `None`.

```python
from fio_wrapper import FIO

# no timeout set, uses default (10 seconds)
fio = FIO()


# Call will timeout after default (10 seconds) from Adapter
all_buildings = fio.Building.all()

# Call will timeout after 3.5 seconds
all_exchange = fio.Exchange.all(timeout=3.5)

```

It is highly recommended to not set any timeout to `None` to avoid infinite loops especially on expensive FIO endpoints like [`Group`](endpoints/group.md).