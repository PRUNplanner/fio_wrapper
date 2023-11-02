class AbstractPlanet:
    def get(self, planet: str):
        raise NotImplementedError()

    def all(self):
        raise NotImplementedError()

    def full(self):
        raise NotImplementedError()

    def sites(self, planet: str):
        raise NotImplementedError()
