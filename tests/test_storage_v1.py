import pytest
from typing import Dict
from fio_wrapper.exceptions import NoStorageData, NotAuthenticated
from fio_wrapper.fio import FIO
from fio_wrapper.models import storage_models

from fio_wrapper.models.storage_models import Storage as StorageModel, StorageList
from .fixtures import ftx_fio_key

storage_item_data = {
    "MaterialId": "4fca6f5b5e6c3b8a1b887c6dc99db146",
    "MaterialName": "drinkingWater",
    "MaterialTicker": "DW",
    "MaterialCategory": "3f047ec3043bdd795fd7272d6be98799",
    "MaterialWeight": 0.10000000149011612,
    "MaterialVolume": 0.10000000149011612,
    "MaterialAmount": 1431,
    "MaterialValue": 26633.2,
    "MaterialValueCurrency": "NCC",
    "Type": "INVENTORY",
    "TotalWeight": 143.10000610351562,
    "TotalVolume": 143.10000610351562,
}

store_data = {
    "StorageItems": [storage_item_data, storage_item_data],
    "StorageId": "00e14a526b92f0c7675732f90b0a2aeb",
    "AddressableId": "6eab22c0630c8081c4be75986dcb0780",
    "Name": None,
    "WeightLoad": 4018.305908203125,
    "WeightCapacity": 6500.0,
    "VolumeLoad": 2312.14990234375,
    "VolumeCapacity": 6500.0,
    "FixedStore": False,
    "Type": "STORE",
    "UserNameSubmitted": "SFSCORPIO",
    "Timestamp": "2023-11-06T08:11:11.524793",
}


@pytest.fixture
def storage_item() -> Dict:
    return storage_item_data


@pytest.fixture
def store() -> Dict:
    return store_data


# Models


def test_model_StorageList(store) -> None:
    data = StorageList.model_validate([store, store])
    for store in data:
        assert type(store) is StorageModel


# Endpoints


@pytest.mark.parametrize(
    "username, mock_status, json_data, return_data",
    [
        (
            "foo",
            200,
            [store_data, store_data],
            StorageList.model_validate([store_data, store_data]),
        ),
        (
            "foo",
            204,
            None,
            NoStorageData,
        ),
        (
            "foo",
            401,
            None,
            NotAuthenticated,
        ),
    ],
)
def test_storage_get(
    requests_mock, ftx_fio_key: FIO, username, mock_status, json_data, return_data
) -> None:
    requests_mock.get(
        ftx_fio_key._adapter.urls.storage_get_url(username=username),
        status_code=mock_status,
        json=json_data,
    )

    if return_data not in [NoStorageData, NotAuthenticated]:
        data = ftx_fio_key.Storage.get(username=username)

        assert data == return_data
    else:
        with pytest.raises(return_data):
            ftx_fio_key.Storage.get(username=username)


@pytest.mark.parametrize(
    "username, specific, mock_status, json_data, return_data",
    [
        (
            "foo",
            "moo",
            200,
            store_data,
            StorageModel.model_validate(store_data),
        ),
        (
            "foo",
            "moo",
            204,
            None,
            NoStorageData,
        ),
        (
            "foo",
            "moo",
            401,
            None,
            NotAuthenticated,
        ),
    ],
)
def test_storage_get_specific(
    requests_mock,
    ftx_fio_key: FIO,
    username,
    specific,
    mock_status,
    json_data,
    return_data,
) -> None:
    requests_mock.get(
        ftx_fio_key._adapter.urls.storage_get_specific_url(
            username=username, specific=specific
        ),
        status_code=mock_status,
        json=json_data,
    )

    if return_data not in [NoStorageData, NotAuthenticated]:
        data = ftx_fio_key.Storage.get_specific(username=username, specific=specific)

        assert data == return_data
    else:
        with pytest.raises(return_data):
            ftx_fio_key.Storage.get_specific(username=username, specific=specific)


@pytest.mark.parametrize(
    "username, mock_status, json_data, return_data",
    [
        (
            "foo",
            200,
            ["abc", "def"],
            ["abc", "def"],
        ),
        (
            "foo",
            204,
            None,
            NoStorageData,
        ),
        (
            "foo",
            401,
            None,
            NotAuthenticated,
        ),
    ],
)
def test_storage_planets(
    requests_mock,
    ftx_fio_key: FIO,
    username,
    mock_status,
    json_data,
    return_data,
) -> None:
    requests_mock.get(
        ftx_fio_key._adapter.urls.storage_planets_get_url(username=username),
        status_code=mock_status,
        json=json_data,
    )

    if return_data not in [NoStorageData, NotAuthenticated]:
        data = ftx_fio_key.Storage.planets(username=username)

        assert data == return_data
    else:
        with pytest.raises(return_data):
            ftx_fio_key.Storage.planets(username=username)
