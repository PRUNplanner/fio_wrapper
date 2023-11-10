from typing import Optional


class AbstractBuilding:
    def get(self, building_ticker: str, timeout: Optional[float] = None):
        raise NotImplementedError()

    def allbuildings(self, timeout: Optional[float] = None):
        raise NotImplementedError()
