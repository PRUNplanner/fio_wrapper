from fio_wrapper.fio_adapter import FIOAdapter
from fio_wrapper.urls import URLs


class AbstractEndpoint:
    def __init__(self, adapter: FIOAdapter, urls: URLs) -> None:
        self.adapter: FIOAdapter = adapter
        self.urls: URLs = urls
