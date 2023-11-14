from functools import wraps

from fio_wrapper.exceptions import NoAPIKeyProvided
from fio_wrapper.fio_adapter import FIOAdapter


def apikey_required(func) -> any:
    """Wraps endpoint and check for FIO API Key

    Args:
        func (method): Wrapped endpoint method

    Raises:
        SystemExit: Decorator can only be used on endpoints
        NoAPIKeyProvided: FIO API Key not provided, but endpoint requires it.

    Returns:
        method: Executed endpoint method
    """

    @wraps(func)
    def wrapper_apikey_required(self, *args, **kwargs):
        # can only decorate endpoint functions
        if self.adapter is None or not isinstance(self.adapter, FIOAdapter):
            raise SystemExit("apikey_required decorator can only be used on endpoints")

        # requires API Key set in adapter
        if self.adapter.header is None or self.adapter.header["Authorization"] is None:
            raise NoAPIKeyProvided(
                "FIO API Key not provided. This endpoint requires an API key."
            )

        return func(self, *args, **kwargs)

    return wrapper_apikey_required
