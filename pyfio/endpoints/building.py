from pyfio.fio_adapter import FIOAdapter


class Building:
    def __init__(self, adapter: FIOAdapter) -> None:
        self._adapter: FIOAdapter = adapter

    # /building/allbuildings

    # /building/{BuildingTicker}
