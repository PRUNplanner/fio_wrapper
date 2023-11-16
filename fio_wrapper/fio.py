"""FIO class to access game data through FIO REST API endpoints
"""
from typing import Dict, Optional
from fio_wrapper.config import Config
from fio_wrapper.fio_adapter import FIOAdapter
from fio_wrapper.exceptions import EndpointNotImplemented

from fio_wrapper.endpoints.endpoints_v1 import building as building_v1
from fio_wrapper.endpoints.endpoints_v1 import exchange as exchange_v1
from fio_wrapper.endpoints.endpoints_v1 import localmarket as localmarket_v1
from fio_wrapper.endpoints.endpoints_v1 import material as material_v1
from fio_wrapper.endpoints.endpoints_v1 import planet as planet_v1
from fio_wrapper.endpoints.endpoints_v1 import recipe as recipe_v1
from fio_wrapper.endpoints.endpoints_v1 import sites as sites_v1
from fio_wrapper.endpoints.endpoints_v1 import storage as storage_v1
from fio_wrapper.endpoints.endpoints_v1 import group as group_v1
from fio_wrapper.urls import URLs


class FIO:
    """FIO API wrapper class

    Attributes:
        Building (Building): Building information
        Exchange (Exchange): Exchange information
        Group (Group): Group information
        LocalMarket (LocalMarket): LocalMarket information
        Material (Material): Material information
        Planet (Planet): Planet information
        Recipe (Recipe): Recipe information
        Sites (Sites): Sites information
        Storage (Storage): Storage information

        config (Config): FIO Configuration
        adapter (FIOAdapter): FIO Adapter
        urls (URLs): FIO URLs
    """

    def __init__(
        self,
        version: Optional[str] = None,
        application: Optional[str] = None,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: Optional[float] = None,
        ssl_verify: Optional[bool] = True,
        config: Optional[str] = None,
    ) -> None:
        """Initializes the FIO wrapper

        Args:
            version (str, optional): FIO API version. Defaults to None.
            application (str, optional): Application name. Defaults to None.
            api_key (str, optional): FIO API-Key. Defaults to None.
            base_url (str, optional): FIO base url. Defaults to None.
            timeout (float, optional): Request timeout. Defaults to None.
            ssl_verify (bool, optional): Verify https connection. Defaults to True.
            config: (str, optional): User specified configuration file. Defaults to None.

        Raises:
            EndpointNotImplemented: _description_
        """

        # Config needs to already supercede here !!!

        self.config = Config(
            api_key=api_key,
            version=version,
            application=application,
            base_url=base_url,
            timeout=timeout,
            ssl_verify=ssl_verify,
            user_config=config,
        )

        # Check version availability
        if self.config.version not in self.config.versions:
            raise EndpointNotImplemented("FIO version not supported")

        # create adapter
        self.adapter = FIOAdapter(header=self.get_header(), config=self.config)

        # create urls
        self.urls: URLs = URLs(self.config)

        # add version 1.0.0 endpoints
        if self.config.version == "1.0.0":
            self.Building = building_v1.Building(self.adapter, self.urls)
            self.Exchange = exchange_v1.Exchange(self.adapter, self.urls)
            self.Group = group_v1.Group(self.adapter, self.urls)
            self.LocalMarket = localmarket_v1.LocalMarket(self.adapter, self.urls)
            self.Material = material_v1.Material(self.adapter, self.urls)
            self.Planet = planet_v1.Planet(self.adapter, self.urls)
            self.Recipe = recipe_v1.Recipe(self.adapter, self.urls)
            self.Sites = sites_v1.Sites(self.adapter, self.urls)
            self.Storage = storage_v1.Storage(self.adapter, self.urls)

    def get_header(self) -> Dict[str, str]:
        """Creates the header to be included in calls towards FIO

        Returns:
            Dict[str, str]: Contains "Authorization" and "X-FIO-Application"
        """
        return {
            "Authorization": self.config.api_key,
            "X-FIO-Application": self.config.application,
        }
