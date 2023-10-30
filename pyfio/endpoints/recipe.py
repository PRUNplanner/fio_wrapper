from pyfio.fio_adapter import FIOAdapter


class Recipe:
    def __init__(self, adapter: FIOAdapter) -> None:
        self._adapter: FIOAdapter = adapter

    # /recipes/{Ticker}
    # /recipes/allrecipes
