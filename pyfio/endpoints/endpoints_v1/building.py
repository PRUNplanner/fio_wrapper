from pyfio.endpoints.abstracts.abstract_building import AbstractBuilding
from pyfio.fio_adapter import FIOAdapter


class Building(AbstractBuilding):
    def __init__(self, adapter: FIOAdapter) -> None:
        self._adapter: FIOAdapter = adapter

    # /building/allbuildings

    # /building/{BuildingTicker}
