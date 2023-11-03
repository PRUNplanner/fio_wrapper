"""Access planet information from FIO.
"""
from typing import List
from fio_wrapper.endpoints.abstracts.abstract_planet import AbstractPlanet
from fio_wrapper.exceptions import (
    PlanetNotFound,
    PlanetSearchDistanceChecksInvalid,
    PlanetSearchInvalidRequest,
    PlanetSearchMaterialsInvalid,
)
from fio_wrapper.fio_adapter import FIOAdapter
from fio_wrapper.models.planet_models import (
    PlanetFull,
    PlanetFullList,
    PlanetList,
    PlanetSiteList,
)
from fio_wrapper.validators import (
    validate_planet_search_distance_checks,
    validate_planet_search_materials,
)


class Planet(AbstractPlanet):
    """Planet endpoint wrapper"""

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

    # /planet/search
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
    ) -> PlanetFullList:
        """Performs a search request towards FIO to find a planet matching the search parameters

        Args:
            materials (List[str], optional): List of materials to search for, e.g. ["FEO", "LST"].
            include_rocky (bool, optional): Planet can be Rocky.
            include_gaseous (bool, optional): Planet can be Gaseous.
            include_low_gravity (bool, optional): Planet can be low gravity.
            include_high_gravity (bool, optional): Planet can be high gravity.
            include_low_pressure (bool, optional): Planet can be low pressure.
            include_high_pressure (bool, optional): Planet can be high pressure.
            include_low_temperature (bool, optional): Planet can be low temperature.
            include_high_temperature (bool, optional): Planet can be high temperature.
            must_be_fertile (bool, optional): Planet must be Fertile.
            must_have_localmarket (bool, optional): Planet must have a Local Market.
            must_have_cogc (bool, optional): Planet must have a Chamber of Glboal Commerce.
            must_have_war (bool, optional): Planet must have warehouses.
            must_have_adm (bool, optional): Planet must have a Planetary Administration Center.
            must_have_shy (bool, optional): Planet must have a Shipyard.
            distance_checks (List[str], optional): List of other planets to check distance to, e.g. ["ANT", "MOR"].

        Raises:
            PlanetSearchMaterialsInvalid: _description_
            PlanetSearchDistanceChecksInvalid: _description_
            PlanetSearchInvalidRequest: _description_

        Returns:
            PlanetFullList: List of Planets with full information as List[PlanetFull]
        """
        if not validate_planet_search_materials(materials=materials):
            raise PlanetSearchMaterialsInvalid(
                "Invalid materials provided. Can check for up to 4 materials."
            )

        if not validate_planet_search_distance_checks(distance_checks=distance_checks):
            raise PlanetSearchDistanceChecksInvalid(
                "Invalid distance checks. Can check for up to 3 distances."
            )

        (status, data) = self._adapter.post(
            endpoint=self._adapter.urls.planet_search_url(),
            data={
                "Materials": materials,
                "IncludeRocky": include_rocky,
                "IncludeGaseous": include_gaseous,
                "IncludeLowGravity": include_low_gravity,
                "IncludeHighGravity": include_high_gravity,
                "IncludeLowPressure": include_low_pressure,
                "IncludeHighPressure": include_high_pressure,
                "IncludeLowTemperature": include_low_temperature,
                "IncludeHighTemperature": include_high_temperature,
                "MustBeFertile": must_be_fertile,
                "MustHaveLocalMarket": must_have_localmarket,
                "MustHaveChamberOfCommerce": must_have_cogc,
                "MustHaveWarehouse": must_have_war,
                "MustHaveAdministrationCenter": must_have_adm,
                "MustHaveShipyard": must_have_shy,
                "DistanceChecks": distance_checks,
            },
            err_codes=[400],
        )

        if status == 200:
            return PlanetFullList.model_validate(data)
        elif status == 400:
            raise PlanetSearchInvalidRequest("Failed to parse payload")
