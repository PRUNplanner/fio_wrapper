# Caching

Out of the box FIO Wrapper does not include any form of caching for FIO requests. As this can be extremely helpful to minimize load on FIO and wait times you can install the wrapper with `cache` extra.

## Installation of FIO Wrapper with Cache Extra
```python
pip install fio-wrapper[cache]
```

FIO Wrapper will now make use of [requests-cache](https://requests-cache.readthedocs.io/en/stable/index.html) as persistent HTTP cache on top of Pythons `requests` library. This package will only use `memory` caching.

## Cache configuration
Caching can only be enabled with a [user configuration file](config.md) provided when instantiating the `FIO` wrapper. 

### Minimal
There are two minimal configuration options to be set:

```yaml
cache:
  enabled: true
  default_expire: 3600 
```

This user configuration enables the caching of requests and sets the default expiration to 10 seconds.

### Advanced

You are able to provide URL patterns matching [integrated endpoints](routes.md) to cache and specify their individual expiration with the following options:

- `int` = Number of Seconds (e.g., `120` = 2 minutes)
- `NEVER_EXPIRE` = route will always use cache and never expire
- `DO_NOT_CACHE` = route will never be cached

A minimal example of caching individual urls:

```yaml
cache:
  urls:
    "*/material/*": 3600
    "*/exchange/all": NEVER_EXPIRE
    "*/exchange/full": DO_NOT_CACHE
```