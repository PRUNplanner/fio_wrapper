class AbstractSites:
    def get(self, username: str):
        raise NotImplementedError()

    def get_planet(self, username: str, planet: str):
        raise NotImplementedError()

    def planets(self, username: str):
        raise NotImplementedError()
