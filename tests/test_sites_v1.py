import pytest
from typing import Dict
from fio_wrapper.exceptions import NoSiteData, NotAuthenticated
from fio_wrapper.fio import FIO

from fio_wrapper.models.sites_models import Site, SiteList, Warehouse, WarehouseList
from .fixtures import ftx_fio_key

warehouse_data = {
    "WarehouseId": "e83d8b9da72479e292363c9d16ade4e5-5d817c73ae8c9c366d1f12da24b80c6e",
    "StoreId": "5d817c73ae8c9c366d1f12da24b80c6e",
    "Units": 10,
    "WeightCapacity": 5000,
    "VolumeCapacity": 5000,
    "NextPaymentTimestampEpochMs": 1699456663947,
    "FeeAmount": 1000,
    "FeeCurrency": "NCC",
    "FeeCollectorId": None,
    "FeeCollectorName": None,
    "FeeCollectorCode": None,
    "LocationName": "Moria Station",
    "LocationNaturalId": "MOR",
    "UserNameSubmitted": "SFSCORPIO",
    "Timestamp": "2023-11-06T08:11:10.766565",
}


@pytest.fixture
def warehouse() -> Dict:
    return warehouse_data


site_data = {
    "Buildings": [
        {
            "ReclaimableMaterials": [
                {
                    "MaterialId": "420b38d32301dfe56403d1f3967d5b86",
                    "MaterialName": "basicDeckElements",
                    "MaterialTicker": "BDE",
                    "MaterialAmount": 3,
                },
                {
                    "MaterialId": "63b98e9700f6630cbfd9c824e0882388",
                    "MaterialName": "basicBulkhead",
                    "MaterialTicker": "BBH",
                    "MaterialAmount": 3,
                },
                {
                    "MaterialId": "6bbdf7d0503153753c8cb23653a4d22b",
                    "MaterialName": "basicStructuralElements",
                    "MaterialTicker": "BSE",
                    "MaterialAmount": 5,
                },
                {
                    "MaterialId": "cc5fb1618f0506e80bfbcee9ae2605ab",
                    "MaterialName": "mineralConstructionGranulate",
                    "MaterialTicker": "MCG",
                    "MaterialAmount": 57,
                },
            ],
            "RepairMaterials": [
                {
                    "MaterialId": "ec3491b37050a8c780dc514033131843",
                    "MaterialName": "hardenedStructuralElements",
                    "MaterialTicker": "HSE",
                    "MaterialAmount": 1,
                },
                {
                    "MaterialId": "cc5fb1618f0506e80bfbcee9ae2605ab",
                    "MaterialName": "mineralConstructionGranulate",
                    "MaterialTicker": "MCG",
                    "MaterialAmount": 11,
                },
                {
                    "MaterialId": "420b38d32301dfe56403d1f3967d5b86",
                    "MaterialName": "basicDeckElements",
                    "MaterialTicker": "BDE",
                    "MaterialAmount": 1,
                },
                {
                    "MaterialId": "63b98e9700f6630cbfd9c824e0882388",
                    "MaterialName": "basicBulkhead",
                    "MaterialTicker": "BBH",
                    "MaterialAmount": 1,
                },
                {
                    "MaterialId": "6bbdf7d0503153753c8cb23653a4d22b",
                    "MaterialName": "basicStructuralElements",
                    "MaterialTicker": "BSE",
                    "MaterialAmount": 1,
                },
            ],
            "SiteBuildingId": "848dbfa8427430106b693352338747cd-e79830eee974fc63e91a92989db7cb91",
            "BuildingId": "e79830eee974fc63e91a92989db7cb91",
            "BuildingCreated": 1680875562016,
            "BuildingName": "smelter",
            "BuildingTicker": "SME",
            "BuildingLastRepair": 1696857185624,
            "Condition": 0.9962850213050842,
        },
        {
            "ReclaimableMaterials": [],
            "RepairMaterials": [],
            "SiteBuildingId": "848dbfa8427430106b693352338747cd-e7df7919388409e07c480f4b3f7f616a",
            "BuildingId": "e7df7919388409e07c480f4b3f7f616a",
            "BuildingCreated": 1680875676626,
            "BuildingName": "habitationPioneer",
            "BuildingTicker": "HB1",
            "BuildingLastRepair": None,
            "Condition": 0.3319239914417267,
        },
        {
            "ReclaimableMaterials": [
                {
                    "MaterialId": "772408d48cf5842fb003698aaa7a6a94",
                    "MaterialName": "lightweightBulkhead",
                    "MaterialTicker": "LBH",
                    "MaterialAmount": 1,
                },
                {
                    "MaterialId": "63b98e9700f6630cbfd9c824e0882388",
                    "MaterialName": "basicBulkhead",
                    "MaterialTicker": "BBH",
                    "MaterialAmount": 1,
                },
                {
                    "MaterialId": "3010d90fde69729f4754b092fdcda826",
                    "MaterialName": "lightweightDeckElements",
                    "MaterialTicker": "LDE",
                    "MaterialAmount": 1,
                },
                {
                    "MaterialId": "cc5fb1618f0506e80bfbcee9ae2605ab",
                    "MaterialName": "mineralConstructionGranulate",
                    "MaterialTicker": "MCG",
                    "MaterialAmount": 84,
                },
                {
                    "MaterialId": "ec53c7423b75ca0d868f9580ae921561",
                    "MaterialName": "truss",
                    "MaterialTicker": "TRU",
                    "MaterialAmount": 3,
                },
            ],
            "RepairMaterials": [
                {
                    "MaterialId": "ec53c7423b75ca0d868f9580ae921561",
                    "MaterialName": "truss",
                    "MaterialTicker": "TRU",
                    "MaterialAmount": 1,
                },
                {
                    "MaterialId": "ec3491b37050a8c780dc514033131843",
                    "MaterialName": "hardenedStructuralElements",
                    "MaterialTicker": "HSE",
                    "MaterialAmount": 1,
                },
                {
                    "MaterialId": "cc5fb1618f0506e80bfbcee9ae2605ab",
                    "MaterialName": "mineralConstructionGranulate",
                    "MaterialTicker": "MCG",
                    "MaterialAmount": 16,
                },
                {
                    "MaterialId": "3010d90fde69729f4754b092fdcda826",
                    "MaterialName": "lightweightDeckElements",
                    "MaterialTicker": "LDE",
                    "MaterialAmount": 1,
                },
                {
                    "MaterialId": "772408d48cf5842fb003698aaa7a6a94",
                    "MaterialName": "lightweightBulkhead",
                    "MaterialTicker": "LBH",
                    "MaterialAmount": 1,
                },
                {
                    "MaterialId": "63b98e9700f6630cbfd9c824e0882388",
                    "MaterialName": "basicBulkhead",
                    "MaterialTicker": "BBH",
                    "MaterialAmount": 1,
                },
            ],
            "SiteBuildingId": "848dbfa8427430106b693352338747cd-ed76854330a83dc6eabc512397cd832a",
            "BuildingId": "ed76854330a83dc6eabc512397cd832a",
            "BuildingCreated": 1680955853542,
            "BuildingName": "fineSmithy",
            "BuildingTicker": "FS",
            "BuildingLastRepair": 1696857185624,
            "Condition": 0.9962850213050842,
        },
        {
            "ReclaimableMaterials": [],
            "RepairMaterials": [],
            "SiteBuildingId": "848dbfa8427430106b693352338747cd-fcf8167cf196163a9f1c7d5561891f24",
            "BuildingId": "fcf8167cf196163a9f1c7d5561891f24",
            "BuildingCreated": 1680875522442,
            "BuildingName": "habitationPioneer",
            "BuildingTicker": "HB1",
            "BuildingLastRepair": None,
            "Condition": 0.3319239914417267,
        },
    ],
    "SiteId": "848dbfa8427430106b693352338747cd",
    "PlanetId": "18e09634754ddf9e63b76089b79176e2",
    "PlanetIdentifier": "ZV-759b",
    "PlanetName": "Vulcan",
    "PlanetFoundedEpochMs": 1680875346445,
    "InvestedPermits": 2,
    "MaximumPermits": 3,
    "UserNameSubmitted": "SFSCORPIO",
    "Timestamp": "2023-11-06T08:11:15.205435",
}


@pytest.fixture
def site() -> Dict:
    return site_data


# Models


def test_site_list(site) -> None:
    data = SiteList.model_validate([site, site])

    for site in data:
        assert type(site) == Site


def test_warehouse_list(warehouse) -> None:
    data = WarehouseList.model_validate([warehouse, warehouse])

    for warehouse in data:
        assert type(warehouse) == Warehouse


# Endpoints


@pytest.mark.parametrize(
    "username, planet, mock_url, mock_status, json_data, return_data",
    [
        (
            "foo",
            None,
            FIO(api_key="abc")._adapter.urls.sites_get_url(username="foo"),
            200,
            [site_data, site_data],
            SiteList.model_validate([site_data, site_data]),
        ),
        (
            "foo",
            "moo",
            FIO(api_key="abc")._adapter.urls.sites_planets_get_planet_url(
                username="foo", planet="moo"
            ),
            200,
            site_data,
            Site.model_validate(site_data),
        ),
        (
            "foo",
            None,
            FIO(api_key="abc")._adapter.urls.sites_get_url(username="foo"),
            204,
            None,
            NoSiteData,
        ),
    ],
)
def test_sites_get(
    requests_mock,
    ftx_fio_key: FIO,
    username,
    planet,
    mock_url,
    mock_status,
    json_data,
    return_data,
) -> None:
    requests_mock.get(mock_url, status_code=mock_status, json=json_data)

    if return_data not in [NoSiteData, NotAuthenticated]:
        data = ftx_fio_key.Sites.get(username=username, planet=planet)

        assert data == return_data

    else:
        with pytest.raises(return_data):
            ftx_fio_key.Sites.get(username=username, planet=planet)


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
            NoSiteData,
        ),
        (
            "foo",
            401,
            None,
            NotAuthenticated,
        ),
    ],
)
def test_planets(
    requests_mock, ftx_fio_key: FIO, username, mock_status, json_data, return_data
) -> None:
    requests_mock.get(
        ftx_fio_key._adapter.urls.sites_planets_get_url(username=username),
        status_code=mock_status,
        json=json_data,
    )

    if return_data not in [NoSiteData, NotAuthenticated]:
        data = ftx_fio_key.Sites.planets(username=username)
        assert data == return_data

    else:
        with pytest.raises(return_data):
            ftx_fio_key.Sites.planets(username=username)


@pytest.mark.parametrize(
    "username, mock_status, json_data, return_data",
    [
        (
            "foo",
            200,
            [warehouse_data, warehouse_data],
            WarehouseList.model_validate([warehouse_data, warehouse_data]),
        ),
        (
            "foo",
            204,
            None,
            NoSiteData,
        ),
        (
            "foo",
            401,
            None,
            NotAuthenticated,
        ),
    ],
)
def test_warehouses(
    requests_mock, ftx_fio_key: FIO, username, mock_status, json_data, return_data
) -> None:
    requests_mock.get(
        ftx_fio_key._adapter.urls.sites_warehouses_get(username=username),
        status_code=mock_status,
        json=json_data,
    )

    if return_data not in [NoSiteData, NotAuthenticated]:
        data = ftx_fio_key.Sites.warehouses(username=username)
        assert data == return_data

    else:
        with pytest.raises(return_data):
            ftx_fio_key.Sites.warehouses(username=username)
