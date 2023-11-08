from typing import Dict
import pytest
from fio_wrapper.exceptions import UnknownFIOResponse
from fio_wrapper.fio import FIO
from .fixtures import ftx_fio_key

from fio_wrapper.models.group_models import (
    Group,
    GroupHub,
    GroupUser,
    GroupAdmin,
    GroupList,
    GroupMembership,
    GroupMembershipList,
    BurnList,
    Burn,
)

# Model

group_data: Dict = {
    "GroupAdmins": [{"GroupAdminUserName": "admin"}],
    "GroupUsers": [
        {"GroupUserName": "user_1"},
        {"GroupUserName": "user_2"},
        {"GroupUserName": "user_3"},
        {"GroupUserName": "admin"},
    ],
    "GroupModelId": 12345678,
    "GroupOwner": "admin",
    "GroupName": "fiowrapper",
}

membership_data: Dict = {"GroupName": "FIOWRAP", "GroupId": 12345678}

hub_data: Dict = {
    "GroupName": None,
    "CXWarehouses": [],
    "PlayerShipsInFlight": [],
    "PlayerStationaryShips": [],
    "Failures": [],
}

burn_data: Dict = {
    "RequesterUserName": "foo",
    "UserName": "moo",
    "Error": None,
    "PlanetId": None,
    "PlanetName": None,
    "PlanetNaturalId": None,
    "PlanetConsumptionTime": "2023-11-08T04:30:38.497881",
    "LastUpdate": "2023-11-08T05:46:03.732036",
    "LastUpdateCause": "STORAGE",
    "Inventory": [],
    "WorkforceConsumption": [],
    "OrderConsumption": [],
    "OrderProduction": [],
}


@pytest.fixture
def group_1() -> Group:
    return Group.model_validate(group_data)


@pytest.fixture
def membership_1() -> GroupMembership:
    return GroupMembership.model_validate(membership_data)


@pytest.fixture
def hub_1() -> GroupHub:
    return GroupHub.model_validate(hub_data)


@pytest.fixture
def groupmembership_1() -> GroupMembership:
    return GroupMembership(GroupName="foo", GroupId=123)


@pytest.fixture
def burn_1() -> Burn:
    return Burn.model_validate(burn_data)


def test_model_Group_users(group_1) -> None:
    data = group_1

    assert data.users() == ["USER_1", "USER_2", "USER_3", "ADMIN"]


def test_model_GroupList(group_1) -> None:
    data = GroupList.model_validate([group_1, group_1])

    for group in data:
        assert type(group) is Group

    assert data.ids() == [12345678, 12345678]


def test_model_GroupMembershipList(groupmembership_1) -> None:
    data = GroupMembershipList.model_validate([groupmembership_1, groupmembership_1])

    for membership in data:
        assert type(membership) is GroupMembership

    assert data.ids() == [123, 123]


def test_model_Burn() -> None:
    data = BurnList.model_validate([])

    for burn in data:
        assert type(burn) is Burn


# Endpoints


@pytest.mark.parametrize(
    "mock_status, json_data, return_data",
    [
        (
            200,
            [group_data, group_data],
            GroupList.model_validate([group_data, group_data]),
        ),
        (
            500,
            None,
            UnknownFIOResponse,
        ),
    ],
)
def test_group_all(
    requests_mock, ftx_fio_key: FIO, mock_status, json_data, return_data
) -> None:
    requests_mock.get(
        ftx_fio_key._adapter.urls.group_all_url(),
        status_code=mock_status,
        json=json_data,
    )

    if return_data is not UnknownFIOResponse:
        data = ftx_fio_key.Group.all()

        assert data == return_data
    else:
        with pytest.raises(return_data):
            ftx_fio_key.Group.all()


@pytest.mark.parametrize(
    "groupid, mock_status, json_data, return_data",
    [
        (
            12345678,
            200,
            group_data,
            Group.model_validate(group_data),
        ),
        (
            12345678,
            500,
            None,
            UnknownFIOResponse,
        ),
    ],
)
def test_group_get(
    requests_mock, ftx_fio_key: FIO, groupid, mock_status, json_data, return_data
) -> None:
    requests_mock.get(
        ftx_fio_key._adapter.urls.group_get_url(groupid=groupid),
        status_code=mock_status,
        json=json_data,
    )

    if return_data is not UnknownFIOResponse:
        data = ftx_fio_key.Group.get(groupid=groupid)

        assert data == return_data
    else:
        with pytest.raises(return_data):
            ftx_fio_key.Group.get(groupid=groupid)


@pytest.mark.parametrize(
    "mock_status, json_data, return_data",
    [
        (
            200,
            [membership_data, membership_data],
            GroupMembershipList.model_validate([membership_data, membership_data]),
        ),
        (
            500,
            None,
            UnknownFIOResponse,
        ),
    ],
)
def test_group_memberships(
    requests_mock, ftx_fio_key: FIO, mock_status, json_data, return_data
) -> None:
    requests_mock.get(
        ftx_fio_key._adapter.urls.group_memberships_url(),
        status_code=mock_status,
        json=json_data,
    )

    if return_data is not UnknownFIOResponse:
        data = ftx_fio_key.Group.memberships()

        assert data == return_data
    else:
        with pytest.raises(return_data):
            ftx_fio_key.Group.memberships()


@pytest.mark.parametrize(
    "members, mock_status, json_data, return_data",
    [
        (
            ["foo", "moo"],
            200,
            hub_data,
            GroupHub.model_validate(hub_data),
        ),
        (
            ["foo", "moo"],
            500,
            None,
            UnknownFIOResponse,
        ),
    ],
)
def test_group_hub(
    requests_mock, ftx_fio_key: FIO, members, mock_status, json_data, return_data
) -> None:
    requests_mock.post(
        ftx_fio_key._adapter.urls.group_hub_url(),
        status_code=mock_status,
        json=json_data,
    )

    if return_data is not UnknownFIOResponse:
        data = ftx_fio_key.Group.hub(members=members)

        assert data == return_data
    else:
        with pytest.raises(return_data):
            ftx_fio_key.Group.hub(members=members)


@pytest.mark.parametrize(
    "groupid, mock_status, json_data, return_data",
    [
        (
            123,
            200,
            [burn_data, burn_data],
            BurnList.model_validate([burn_data, burn_data]),
        ),
        (
            123,
            500,
            None,
            UnknownFIOResponse,
        ),
    ],
)
def test_group_burn(
    requests_mock, ftx_fio_key: FIO, groupid, mock_status, json_data, return_data
) -> None:
    requests_mock.get(
        ftx_fio_key._adapter.urls.group_burn_url(groupid=groupid),
        status_code=mock_status,
        json=json_data,
    )

    if return_data is not UnknownFIOResponse:
        data = ftx_fio_key.Group.burn(groupid=groupid)

        assert data == return_data
    else:
        with pytest.raises(return_data):
            ftx_fio_key.Group.burn(groupid=groupid)
