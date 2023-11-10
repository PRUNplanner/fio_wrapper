"""Access site information from FIO.
"""

from typing import List, Optional
from fio_wrapper.endpoints.abstracts.abstract_endpoint import AbstractEndpoint
from fio_wrapper.endpoints.abstracts.abstract_sites import AbstractSites
from fio_wrapper.decorator import apikey_required
from fio_wrapper.exceptions import NoSiteData, NotAuthenticated
from fio_wrapper.models.sites_models import Site, SiteList, WarehouseList


class Sites(AbstractSites, AbstractEndpoint):
    @apikey_required
    def get(self, username: str, timeout: Optional[float] = None) -> SiteList:
        """Gets site data for given username from FIO

        Note:
            FIO API Key Required

        Args:
            username (str): Prosperous Universe username
            timeout (float, optional): Request timeout in seconds. Defaults to None.

        Raises:
            NoSiteData: Username has no site data
            NotAuthenticated: Not authenticated or no appropiate permissions

        Returns:
            Site | SiteList: Site or List of Sites
        """

        (status, data) = self._adapter.get(
            endpoint=self._adapter.urls.sites_get_url(username=username),
            err_codes=[204, 401],
            timeout=timeout,
        )

        if status == 200:
            return SiteList.model_validate(data)

        elif status == 204:
            raise NoSiteData("Username has no site data")
        elif status == 401:
            raise NotAuthenticated("Not authenticated or no appropiate permissions")

    @apikey_required
    def get_planet(
        self, username: str, planet: str, timeout: Optional[float] = None
    ) -> Site:
        """Gets site data for given username and planet from FIO

        Note:
            FIO API Key Required

        Args:
            username (str): Prosperous Universe username
            planet (str): PlanetId, PlanetNaturalId or PlanetName. Defaults to None.
            timeout (float, optional): Request timeout in seconds. Defaults to None.

        Raises:
            NoSiteData: Username has no site data
            NotAuthenticated: Not authenticated or no appropiate permissions

        Returns:
            Site: Site
        """

        (status, data) = self._adapter.get(
            endpoint=self._adapter.urls.sites_planets_get_planet_url(
                username=username, planet=planet
            ),
            err_codes=[204, 401],
            timeout=timeout,
        )

        if status == 200:
            return Site.model_validate(data)
        elif status == 204:
            raise NoSiteData("Username has no site data")
        elif status == 401:
            raise NotAuthenticated("Not authenticated or no appropiate permissions")

    @apikey_required
    def planets(self, username: str, timeout: Optional[float] = None) -> List[str]:
        """Gets a list of SiteIds from FIO for given username

        Note:
            FIO API Key Required

        Args:
            username (str): Prosperous Universe username
            timeout (float, optional): Request timeout in seconds. Defaults to None.

        Raises:
            NoSiteData: Username has no site data
            NotAuthenticated: Not authenticated or no appropiate permissions

        Returns:
            List[str]: List of SiteIds
        """
        (status, data) = self._adapter.get(
            endpoint=self._adapter.urls.sites_planets_get_url(username=username),
            err_codes=[204, 401],
            timeout=timeout,
        )

        if status == 200:
            return data
        elif status == 204:
            raise NoSiteData("Username has no site data")
        elif status == 401:
            raise NotAuthenticated("Not authenticated or no appropiate permissions")

    @apikey_required
    def warehouses(
        self, username: str, timeout: Optional[float] = None
    ) -> WarehouseList:
        """Get warehouse data for username from FIO

        Note:
            FIO API Key Required

        Args:
            username (str): Prosperous Universe username
            timeout (float, optional): Request timeout in seconds. Defaults to None.

        Raises:
            NoSiteData: Username has no warehouse site data
            NotAuthenticated: Not authenticated or no appropiate permissions

        Returns:
            WarehouseList: List of Warehouses
        """
        (status, data) = self._adapter.get(
            endpoint=self._adapter.urls.sites_warehouses_get(username=username),
            err_codes=[204, 401],
            timeout=timeout,
        )

        if status == 200:
            return WarehouseList.model_validate(data)
        elif status == 204:
            raise NoSiteData("Username has no warehouse site data")
        elif status == 401:
            raise NotAuthenticated("Not authenticated or no appropiate permissions")
