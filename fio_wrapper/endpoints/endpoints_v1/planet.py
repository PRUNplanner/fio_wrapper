from fio_wrapper.endpoints.abstracts.abstract_planet import AbstractPlanet
from fio_wrapper.exceptions import PlanetNotFound
from fio_wrapper.fio_adapter import FIOAdapter
from fio_wrapper.models.planet_models import (
    PlanetFull,
    PlanetFullList,
    PlanetList,
    PlanetSiteList,
)


class Planet(AbstractPlanet):
    def __init__(self, adapter: FIOAdapter) -> None:
        self._adapter: FIOAdapter = adapter

    # /planet/{Planet}
    def get(self, planet: str) -> PlanetFull:
        """Gets full planet data from FIO

        Args:
            planet (str): PlanetId, PlanetNaturalId or PlanetName

        Raises:
            PlanetNotFound: Planet not found

        Returns:
            PlanetFull: Full planet information
        """
        (status, data) = self._adapter.get(
            endpoint=self._adapter.urls.planet_get_url(planet=planet)
        )

        if status == 200:
            return PlanetFull.model_validate(data)
        elif status == 204:
            raise PlanetNotFound("Planet not found")

    # /planet/allplanets
    def all(self) -> PlanetList:
        """Gets a list of all Planets with minimal information from FIO

        Returns:
            PlanetList: List of Planets as List[Planet]
        """
        (_, data) = self._adapter.get(endpoint=self._adapter.urls.planet_all_url())

        return PlanetList.model_validate(data)

    # /planet/allplanets/full
    def full(self) -> PlanetFullList:
        """Gets a list of all planets from FIO with full planet information

        Returns:
            PlanetFullList: List of Planets with full information as List[PlanetFull]
        """
        (_, data) = self._adapter.get(endpoint=self._adapter.urls.planet_full_url())

        return PlanetFullList.model_validate(data)

    # /planet/sites/{Planet}
    def sites(self, planet: str) -> PlanetSiteList:
        """Gets a list of sites on the planet from FIO

        Args:
            planet (str): PlanetId, PlanetNaturalId or PlanetName

        Raises:
            PlanetNotFound: Planet not found

        Returns:
            PlanetSiteList: List of Planet sites as List[PlanetSite]
        """
        (status, data) = self._adapter.get(
            endpoint=self._adapter.urls.planet_sites_url(planet=planet)
        )

        if status == 200:
            return PlanetSiteList.model_validate(data)
        elif status == 204:
            raise PlanetNotFound("Planet not found")
