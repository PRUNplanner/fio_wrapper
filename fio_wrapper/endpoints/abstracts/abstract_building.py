class AbstractBuilding:
    def get(self, building_ticker: str):
        raise NotImplementedError()

    def allbuildings(self):
        raise NotImplementedError()
