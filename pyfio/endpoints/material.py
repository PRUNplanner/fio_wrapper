from pyfio.fio_adapter import FIOAdapter

from pyfio.models import MaterialModel, MaterialModelList
from pyfio.exceptions import (
    MaterialTickerNotFound,
    MaterialCategoryNotFound,
    MaterialTickerInvalid,
)


class Material:
    def __init__(self, adapter: FIOAdapter) -> None:
        self._adapter = adapter

    def _validate_ticker(self, material_ticker: str) -> None:
        """Validates a material ticker

        Args:
            material_ticker (str): Material ticker

        Raises:
            MaterialTickerInvalid: Material ticker can't be None type
            MaterialTickerInvalid: Material ticker can't be longer than 3 characters
            MaterialTickerInvalid: Material ticker can't be shorter than 1 character
            MaterialTickerInvalid: Material ticker can't contain spaces
        """
        if material_ticker is None:
            raise MaterialTickerInvalid("Material ticker can't be None type")
        if len(material_ticker) > 3:
            raise MaterialTickerInvalid(
                "Material ticker can't be longer than 3 characters"
            )

        if len(material_ticker) < 1:
            raise MaterialTickerInvalid(
                "Material ticker can't be shorter than 1 characters"
            )

        if " " in material_ticker:
            raise MaterialTickerInvalid("Material ticker can't contain spaces")

    def get(self, material_ticker: str) -> MaterialModel:
        """Gets a single material from FIO

        Args:
            material_ticker (str): Material Ticker (e.g., "DW")

        Raises:
            MaterialTickerNotFound: Material Ticker was not found

        Returns:
            MaterialModel: Material
        """

        self._validate_ticker(material_ticker=material_ticker)

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
        """Gets all materials from FIO

        Returns:
            MaterialModelList: List of Materials as List[MaterialModel]
        """
        (_, data) = self._adapter._do(
            http_method="get",
            endpoint=self._adapter.urls.material_allmaterials_url(),
        )
        return MaterialModelList.model_validate(data)

    def category(self, category_name: str) -> MaterialModelList:
        """Gets all materials of specified category

        Args:
            category_name (str): Category name (e.g., "agricultural products")

        Raises:
            MaterialCategoryNotFound: Category was not found

        Returns:
            MaterialModelList: List of Materials as List[MaterialModel]
        """
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
