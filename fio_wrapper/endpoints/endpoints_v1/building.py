"""Access building information from FIO.
"""
from fio_wrapper.endpoints.abstracts.abstract_building import AbstractBuilding
from fio_wrapper.exceptions import BuildingTickerNotFound
from fio_wrapper.fio_adapter import FIOAdapter
from fio_wrapper.models.building_models import BuildingTicker, BuildingTickerList


class Building(AbstractBuilding):
    def __init__(self, adapter: FIOAdapter) -> None:
        self._adapter: FIOAdapter = adapter

    # /building/{BuildingTicker}
    def get(self, building_ticker: str) -> BuildingTicker:
        """Gets a single building from FIO

        Args:
            building_ticker (str): Building Ticker (e.g., "CHP")

        Raises:
            BuildingTickerNotFound: Building Ticker was not found

        Returns:
            BuildingTicker: Building
        """
        (status, data) = self._adapter.get(
            endpoint=self._adapter.urls.building_get_url(
                building_ticker=building_ticker
            ),
            err_codes=[204],
        )

        if status == 200:
            return BuildingTicker.model_validate(data)
        elif status == 204:
            raise BuildingTickerNotFound("Buildingticker not found")

    # /building/allbuildings
    def all(self) -> BuildingTickerList:
        """Gets all buildings from FIO

        Returns:
            BuildingTickerList: List of Buildings as List[BuildingTicker]
        """
        (_, data) = self._adapter.get(
            endpoint=self._adapter.urls.building_get_all_url()
        )

        return BuildingTickerList.model_validate(data)
