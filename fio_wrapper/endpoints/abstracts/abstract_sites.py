class AbstractSites:
    def get(self, username: str, timeout: float | None = None):
        raise NotImplementedError()

    def get_planet(self, username: str, planet: str, timeout: float | None = None):
        raise NotImplementedError()

    def planets(self, username: str, timeout: float | None = None):
        raise NotImplementedError()
