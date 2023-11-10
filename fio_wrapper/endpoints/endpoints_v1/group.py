from typing import List, Optional
from fio_wrapper.decorator import apikey_required
from fio_wrapper.endpoints.abstracts.abstract_endpoint import AbstractEndpoint
from fio_wrapper.endpoints.abstracts.abstract_group import AbstractGroup
from fio_wrapper.models.group_models import (
    BurnList,
    GroupHub,
    GroupList,
    Group as GroupModel,
    GroupMembershipList,
)


class Group(AbstractGroup, AbstractEndpoint):
    @apikey_required
    def all(self, timeout: Optional[float] = None) -> GroupList:
        """Gets all groups from FIO

        Note:
            FIO API Key Required

        Args:
            timeout (float, optional): Request timeout in seconds. Defaults to None.

        Raises:
            UnknownFIOResponse: FIO returned an unknown response

        Returns:
            GroupList: List of Groups
        """
        (status, data) = self._adapter.get(
            endpoint=self._adapter.urls.group_all_url(), timeout=timeout
        )

        if status == 200:
            return GroupList.model_validate(data)

    @apikey_required
    def get(self, groupid: int, timeout: Optional[float] = None) -> GroupModel:
        """Gets group information for specified GroupID from FIO

        Note:
            FIO API Key Required

        Args:
            groupid (int): GroupModelId
            timeout (float, optional): Request timeout in seconds. Defaults to None.

        Raises:
            UnknownFIOResponse: FIO returned an unknown response

        Returns:
            GroupModel: GroupModel
        """
        (status, data) = self._adapter.get(
            endpoint=self._adapter.urls.group_get_url(groupid=groupid), timeout=timeout
        )

        if status == 200:
            return GroupModel.model_validate(data)

    @apikey_required
    def memberships(self, timeout: Optional[float] = None) -> GroupMembershipList:
        """Gets all groups the FIO API Key is member of

        Note:
            FIO API Key Required

        Args:
            timeout (float, optional): Request timeout in seconds. Defaults to None.

        Raises:
            UnknownFIOResponse: FIO returned an unknown response

        Returns:
            GroupMembershipList: List of Group Memberships
        """
        (status, data) = self._adapter.get(
            endpoint=self._adapter.urls.group_memberships_url(), timeout=timeout
        )

        if status == 200:
            return GroupMembershipList.model_validate(data)

    @apikey_required
    def hub(self, members: List[str], timeout: Optional[float] = None) -> GroupHub:
        """Gets the groups Hub information from FIO

        Note:
            FIO API Key Required

        Args:
            members (List[str]): List of members, e.g. ["NAME1", "NAME2"]
            timeout (float, optional): Request timeout in seconds. Defaults to None.

        Raises:
            UnknownFIOResponse: FIO returned an unknown response

        Returns:
            GroupHub: GroupHub data from FIO
        """
        (status, data) = self._adapter.post(
            endpoint=self._adapter.urls.group_hub_url(), data=members, timeout=timeout
        )

        if status == 200:
            return GroupHub.model_validate(data)

    @apikey_required
    def burn(self, groupid: int, timeout: Optional[float] = None) -> BurnList:
        """Gets the groups Burn information from FIO

        Note:
            FIO API Key Required

        Args:
            groupid (int): GroupModelId
            timeout (float, optional): Request timeout in seconds. Defaults to None.

        Raises:
            UnknownFIOResponse: FIO returned an unknown response

        Returns:
            BurnList: List of Burn data
        """
        (status, data) = self._adapter.get(
            endpoint=self._adapter.urls.group_burn_url(groupid=groupid), timeout=timeout
        )

        if status == 200:
            return BurnList.model_validate(data)
