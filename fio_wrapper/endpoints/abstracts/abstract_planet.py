from typing import List


class AbstractPlanet:
    def get(self, planet: str):
        raise NotImplementedError()

    def all(self):
        raise NotImplementedError()

    def full(self):
        raise NotImplementedError()

    def sites(self, planet: str):
        raise NotImplementedError()

    def search(
        self,
        materials: List[str] = [],
        include_rocky: bool = False,
        include_gaseous: bool = False,
        include_low_gravity: bool = False,
        include_high_gravity: bool = False,
        include_low_pressure: bool = False,
        include_high_pressure: bool = False,
        include_low_temperature: bool = False,
        include_high_temperature: bool = False,
        must_be_fertile: bool = False,
        must_have_localmarket: bool = False,
        must_have_cogc: bool = False,
        must_have_war: bool = False,
        must_have_adm: bool = False,
        must_have_shy: bool = False,
        distance_checks: List[str] = [],
    ):
        raise NotImplementedError()
