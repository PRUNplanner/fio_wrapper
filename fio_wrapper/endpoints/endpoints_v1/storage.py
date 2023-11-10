from typing import List, Optional
from fio_wrapper.decorator import apikey_required
from fio_wrapper.endpoints.abstracts.abstract_endpoint import AbstractEndpoint
from fio_wrapper.endpoints.abstracts.abstract_storage import AbstractStorage
from fio_wrapper.exceptions import NoStorageData, NotAuthenticated
from fio_wrapper.models.storage_models import StorageList, Storage as StorageModel


class Storage(AbstractStorage, AbstractEndpoint):
    @apikey_required
    def get(self, username: str, timeout: Optional[float] = None) -> StorageList:
        """Gets users storage data from FIO

        Note:
            FIO API Key Required

        Args:
            username (str): Prosperous Universe username
            timeout (float, optional): Request timeout in seconds. Defaults to None.

        Raises:
            NoStorageData: Username has no storage data
            NotAuthenticated: Not authenticated or no appropiate permissions

        Returns:
            StorageList: List of storages
        """
        (status, data) = self._adapter.get(
            endpoint=self._adapter.urls.storage_get_url(username=username),
            err_codes=[204, 401],
            timeout=timeout,
        )

        if status == 200:
            return StorageList.model_validate(data)

        elif status == 204:
            raise NoStorageData("Username has no storage data")
        elif status == 401:
            raise NotAuthenticated("Not authenticated or no appropiate permissions")

    @apikey_required
    def get_specific(
        self, username: str, specific: str, timeout: Optional[float] = None
    ) -> StorageModel:
        """Gets users specific storage data from FIO

        Note:
            FIO API Key Required

        Args:
            username (str): Prosperous Universe username
            specific (str): StorageId, PlanetId, PlanetNaturalId or PlanetName
            timeout (float, optional): Request timeout in seconds. Defaults to None.

        Raises:
            NoStorageData: Username has no storage data
            NotAuthenticated: Not authenticated or no appropiate permissions

        Returns:
            StorageModel: Storage data
        """
        (status, data) = self._adapter.get(
            endpoint=self._adapter.urls.storage_get_specific_url(
                username=username, specific=specific
            ),
            err_codes=[204, 401],
            timeout=timeout,
        )

        if status == 200:
            return StorageModel.model_validate(data)

        elif status == 204:
            raise NoStorageData("Username has no storage data")
        elif status == 401:
            raise NotAuthenticated("Not authenticated or no appropiate permissions")

    @apikey_required
    def planets(self, username: str, timeout: Optional[float] = None) -> List[str]:
        """Returns a list of storages from FIO

        Note:
            FIO API Key Required

        Args:
            username (str): Prosperous Universe username
            timeout (float, optional): Request timeout in seconds. Defaults to None.

        Raises:
            NoStorageData: Username has no storage data
            NotAuthenticated: Not authenticated or no appropiate permissions

        Returns:
            List[str]: List of StorageIds
        """
        (status, data) = self._adapter.get(
            endpoint=self._adapter.urls.storage_planets_get_url(username=username),
            err_codes=[204, 401],
            timeout=timeout,
        )

        if status == 200:
            return data
        elif status == 204:
            raise NoStorageData("Username has no storage data")
        elif status == 401:
            raise NotAuthenticated("Not authenticated or no appropiate permissions")
