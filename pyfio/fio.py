from pyfio.fio_adapter import FIOAdapter


from pyfio.models import MaterialModel, MaterialModelList
from pyfio.exceptions import MaterialTickerNotFound, MaterialCategoryNotFound


class Material:
    def __init__(self, adapter: FIOAdapter) -> None:
        self._adapter = adapter

    def get(self, material_ticker: str) -> MaterialModel:
        (status, data) = self._adapter._do(
            http_method="get",
            endpoint=self._adapter.urls.material_get_url(
                material_ticker=material_ticker
            ),
            err_codes=[204],
        )

        if status == 200:
            return MaterialModel.model_validate(data)
        elif status == 204:
            raise MaterialTickerNotFound("Materialticker not found")

    def all(self) -> MaterialModelList:
        (_, data) = self._adapter._do(
            http_method="get",
            endpoint=self._adapter.urls.material_allmaterials_url(),
        )
        return MaterialModelList.model_validate(data)

    def category(self, category_name: str) -> MaterialModelList | Exception:
        (status, data) = self._adapter._do(
            http_method="get",
            endpoint=self._adapter.urls.material_get_category(
                category_name=category_name
            ),
            err_codes=[204],
        )

        if status == 200 and len(data) > 0:
            return MaterialModelList.model_validate(data)
        elif status == 204 or len(data) == 0:
            raise MaterialCategoryNotFound("Material category not found")


class FIO:
    def __init__(
        self,
        api_key: str = "",
        version: str = "1.0.0",
        base_url: str = "https://rest.fnar.net",
        ssl_verify: bool = True,
    ) -> None:
        self._adapter = FIOAdapter(api_key, version, base_url, ssl_verify)

        self.Material = Material(self._adapter)
