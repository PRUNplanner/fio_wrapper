from typing import Optional


class AbstractSites:
    def get(self, username: str, timeout: Optional[float] = None):
        raise NotImplementedError()

    def get_planet(self, username: str, planet: str, timeout: Optional[float] = None):
        raise NotImplementedError()

    def planets(self, username: str, timeout: Optional[float] = None):
        raise NotImplementedError()
