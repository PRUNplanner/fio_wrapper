from fio_wrapper.fio_adapter import FIOAdapter


class AbstractEndpoint:
    def __init__(self, adapter: FIOAdapter) -> None:
        self._adapter: FIOAdapter = adapter
