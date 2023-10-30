from pyfio.fio_adapter import FIOAdapter


class Planet:
    def __init__(self, adapter: FIOAdapter) -> None:
        self._adapter: FIOAdapter = adapter

    # /planet/allplanets
    # /planet/allplanets/full
    # /planet/{Planet}
    # /planet/sites/{Planet}
    # /planet/sitescount/{Planet}
