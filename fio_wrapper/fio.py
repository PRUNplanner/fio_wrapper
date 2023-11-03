"""FIO class to access game data through FIO REST API endpoints
"""

from fio_wrapper.fio_adapter import FIOAdapter
from fio_wrapper.exceptions import EndpointNotImplemented

from fio_wrapper.endpoints.endpoints_v1 import building as building_v1
from fio_wrapper.endpoints.endpoints_v1 import exchange as exchange_v1
from fio_wrapper.endpoints.endpoints_v1 import localmarket as localmarket_v1
from fio_wrapper.endpoints.endpoints_v1 import material as material_v1
from fio_wrapper.endpoints.endpoints_v1 import planet as planet_v1
from fio_wrapper.endpoints.endpoints_v1 import recipe as recipe_v1


class FIO:
    """FIO API wrapper class

    Attributes:
        Building (Building): Building information
        Exchange (Exchange): Exchange information
        LocalMarket (LocalMarket): LocalMarket information
        Material (Material): Material information
        Planet (Planet): Planet information
        Recipe (Recipe): Recipe information

    """

    def __init__(
        self,
        api_key: str = "",
        version: str = "1.0.0",
        base_url: str = "https://rest.fnar.net",
        ssl_verify: bool = True,
    ) -> None:
        """Initializes the FIO wrapper

        Args:
            api_key (str, optional): FIO API-Key. Defaults to "".
            version (str, optional): FIO API version. Defaults to "1.0.0".
            base_url (_type_, optional): FIO base url. Defaults to "https://rest.fnar.net".
            ssl_verify (bool, optional): Verify https connection. Defaults to True.

        Raises:
            EndpointNotImplemented: _description_
        """
        self._adapter = FIOAdapter(api_key, version, base_url, ssl_verify)

        if version == "1.0.0":
            self.Building = building_v1.Building(self._adapter)
            self.Exchange = exchange_v1.Exchange(self._adapter)
            self.LocalMarket = localmarket_v1.LocalMarket(self._adapter)
            self.Material = material_v1.Material(self._adapter)
            self.Planet = planet_v1.Planet(self._adapter)
            self.Recipe = recipe_v1.Recipe(self._adapter)

        else:
            raise EndpointNotImplemented()
