from pyfio.fio_adapter import FIOAdapter
from pyfio.endpoints import building, exchange, localmarket, material, planet, recipe


class FIO:
    def __init__(
        self,
        api_key: str = "",
        version: str = "1.0.0",
        base_url: str = "https://rest.fnar.net",
        ssl_verify: bool = True,
    ) -> None:
        self._adapter = FIOAdapter(api_key, version, base_url, ssl_verify)

        self.Building = building.Building(self._adapter)
        self.Exchange = exchange.Exchange(self._adapter)
        self.LocalMarket = localmarket.LocalMarket(self._adapter)
        self.Material = material.Material(self._adapter)
        self.Planet = planet.Planet(self._adapter)
        self.Recipe = recipe.Recipe(self._adapter)
