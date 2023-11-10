class AbstractBuilding:
    def get(self, building_ticker: str, timeout: float | None = None):
        raise NotImplementedError()

    def allbuildings(self, timeout: float | None = None):
        raise NotImplementedError()
