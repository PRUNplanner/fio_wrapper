from pyfio.fio_adapter import FIOAdapter
from pyfio.endpoints import material
from pyfio.endpoints import exchange


class FIO:
    def __init__(
        self,
        api_key: str = "",
        version: str = "1.0.0",
        base_url: str = "https://rest.fnar.net",
        ssl_verify: bool = True,
    ) -> None:
        self._adapter = FIOAdapter(api_key, version, base_url, ssl_verify)

        self.Material = material.Material(self._adapter)
        self.Exchange = exchange.Exchange(self._adapter)
