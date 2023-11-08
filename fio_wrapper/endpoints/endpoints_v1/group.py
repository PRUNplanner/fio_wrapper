from typing import List
from fio_wrapper.decorator import apikey_required
from fio_wrapper.endpoints.abstracts.abstract_endpoint import AbstractEndpoint
from fio_wrapper.endpoints.abstracts.abstract_group import AbstractGroup
from fio_wrapper.exceptions import UnknownFIOResponse
from fio_wrapper.models.group_models import (
    BurnList,
    GroupHub,
    GroupList,
    Group as GroupModel,
    GroupMembershipList,
)


class Group(AbstractGroup, AbstractEndpoint):
    @apikey_required
    def all(self) -> GroupList:
        """Gets all groups from FIO

        Note:
            FIO API Key Required

        Raises:
            UnknownFIOResponse: FIO returned an unknown response

        Returns:
            GroupList: List of Groups
        """
        (status, data) = self._adapter.get(
            endpoint=self._adapter.urls.group_all_url(),
        )

        if status == 200:
            return GroupList.model_validate(data)
        else:
            raise UnknownFIOResponse()

    @apikey_required
    def get(self, groupid: int) -> GroupModel:
        """Gets group information for specified GroupID from FIO

        Note:
            FIO API Key Required

        Args:
            groupid (int): GroupModelId

        Raises:
            UnknownFIOResponse: FIO returned an unknown response

        Returns:
            GroupModel: GroupModel
        """
        (status, data) = self._adapter.get(
            endpoint=self._adapter.urls.group_get_url(groupid=groupid)
        )

        if status == 200:
            return GroupModel.model_validate(data)
        else:
            raise UnknownFIOResponse()

    @apikey_required
    def memberships(self) -> GroupMembershipList:
        """Gets all groups the FIO API Key is member of

        Note:
            FIO API Key Required

        Raises:
            UnknownFIOResponse: FIO returned an unknown response

        Returns:
            GroupMembershipList: List of Group Memberships
        """
        (status, data) = self._adapter.get(
            endpoint=self._adapter.urls.group_memberships_url()
        )

        if status == 200:
            return GroupMembershipList.model_validate(data)
        else:
            raise UnknownFIOResponse()

    @apikey_required
    def hub(self, members: List[str]) -> GroupHub:
        """Gets the groups Hub information from FIO

        Note:
            FIO API Key Required

        Args:
            members (List[str]): List of members, e.g. ["NAME1", "NAME2"]

        Raises:
            UnknownFIOResponse: FIO returned an unknown response

        Returns:
            GroupHub: GroupHub data from FIO
        """
        (status, data) = self._adapter.post(
            endpoint=self._adapter.urls.group_hub_url(), data=members
        )

        if status == 200:
            return GroupHub.model_validate(data)
        else:
            raise UnknownFIOResponse()

    @apikey_required
    def burn(self, groupid: int) -> BurnList:
        """Gets the groups Burn information from FIO

        Note:
            FIO API Key Required

        Args:
            groupid (int): GroupModelId

        Raises:
            UnknownFIOResponse: FIO returned an unknown response

        Returns:
            BurnList: List of Burn data
        """
        (status, data) = self._adapter.get(
            endpoint=self._adapter.urls.group_burn_url(groupid=groupid)
        )

        if status == 200:
            return BurnList.model_validate(data)
        else:
            raise UnknownFIOResponse()
