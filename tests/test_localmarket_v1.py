from typing import Dict
import pytest

from pyfio.exceptions import PlanetNotFound
from .fixtures import ftx_fio

from pyfio import (
    FIO,
    Ad,
    ShippingAd,
    LocalMarketAdList,
    LocalMarketShippingAdList,
    LocalMarketAds,
)


@pytest.fixture
def ad_1() -> Dict:
    return {
        "ContractNaturalId": 99079,
        "PlanetId": "7f1135f5d7792a058c8be66e7cbcb536",
        "PlanetNaturalId": "OT-580b",
        "PlanetName": "Montem",
        "CreatorCompanyId": "1d4ed0f8acb4856efbee83d868f43032",
        "CreatorCompanyName": "Kofkompany",
        "CreatorCompanyCode": "KOFK",
        "MaterialId": "7aeed35adeb209ebdb4985f451ed3e46",
        "MaterialName": "cottonProcessed",
        "MaterialTicker": "COT",
        "MaterialCategory": "7028d7d532ccd4c6c878b069e7bbb634",
        "MaterialWeight": 0.7699999809265137,
        "MaterialVolume": 1,
        "MaterialAmount": 10,
        "Price": 1000,
        "PriceCurrency": "NCC",
        "DeliveryTime": 3,
        "CreationTimeEpochMs": 1698580835953,
        "ExpiryTimeEpochMs": 1699876835953,
        "MinimumRating": "PENDING",
    }


@pytest.fixture
def shipping_ad_1() -> Dict:
    return {
        "SourceIsGaseous": False,
        "DestinationIsGaseous": False,
        "JumpDistance": 0,
        "ContractNaturalId": 10032,
        "PlanetId": "1deca369a92788b8079e7ac245be66f7",
        "PlanetNaturalId": "ANT",
        "PlanetName": "Antares Station",
        "OriginPlanetId": "1deca369a92788b8079e7ac245be66f7",
        "OriginPlanetNaturalId": "ANT",
        "OriginPlanetName": "Antares Station",
        "DestinationPlanetId": "e4e93a5d20a1d75fb04696279137a0b0",
        "DestinationPlanetNaturalId": "ZV-307b",
        "DestinationPlanetName": "ZV-307b",
        "CargoWeight": 500,
        "CargoVolume": 500,
        "CreatorCompanyId": "f20655069a677b136716105227432764",
        "CreatorCompanyName": "future space services",
        "CreatorCompanyCode": "FSS",
        "PayoutPrice": 2500,
        "PayoutCurrency": "AIC",
        "DeliveryTime": 3,
        "CreationTimeEpochMs": 1698704131223,
        "ExpiryTimeEpochMs": 1699136131223,
        "MinimumRating": "PENDING",
    }


@pytest.fixture
def valid_adlist(ad_1, shipping_ad_1) -> Dict:
    return {
        "BuyingAds": [ad_1, ad_1],
        "SellingAds": [ad_1],
        "ShippingAds": [shipping_ad_1],
    }


# Models
def test_model_LocalMarketAdList(ad_1) -> None:
    data = LocalMarketAdList.model_validate([ad_1, ad_1])
    for ad in data:
        assert type(ad) == Ad


def test_model_LocalMarketShippingAdList(shipping_ad_1) -> None:
    data = LocalMarketShippingAdList.model_validate([shipping_ad_1, shipping_ad_1])
    for ad in data:
        assert type(ad) == ShippingAd


# Endpoints


def test_planet_notfound(requests_mock, ftx_fio: FIO, valid_adlist) -> None:
    planet: str = "FOO"
    requests_mock.get(
        ftx_fio._adapter.urls.localmarket_planet_url(planet=planet), status_code=204
    )

    with pytest.raises(PlanetNotFound):
        ftx_fio.LocalMarket.planet(planet=planet)


def test_planet_valid(requests_mock, ftx_fio: FIO, valid_adlist) -> None:
    planet: str = "FOO"
    requests_mock.get(
        ftx_fio._adapter.urls.localmarket_planet_url(planet=planet),
        status_code=200,
        json=valid_adlist,
    )

    data = ftx_fio.LocalMarket.planet(planet=planet)
    assert type(data) == LocalMarketAds
    assert len(data.BuyingAds) == 2
    assert len(data.SellingAds) == 1
    assert len(data.ShippingAds) == 1
