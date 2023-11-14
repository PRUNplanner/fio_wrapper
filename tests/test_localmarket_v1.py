from typing import Dict
import pytest

from fio_wrapper.exceptions import PlanetNotFound
from .fixtures import ftx_fio

from fio_wrapper import (
    FIO,
    Ad,
    ShippingAd,
    LocalMarketAdList,
    LocalMarketShippingAdList,
    LocalMarketAds,
    PlanetOrAdsNotFound,
    CompanyOrAdsNotFound,
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


def test_planet_notfound(requests_mock, ftx_fio: FIO) -> None:
    planet: str = "FOO"
    requests_mock.get(
        ftx_fio.urls.localmarket_planet_url(planet=planet), status_code=204
    )

    with pytest.raises(PlanetNotFound):
        ftx_fio.LocalMarket.planet(planet=planet)


def test_planet_valid(requests_mock, ftx_fio: FIO, valid_adlist) -> None:
    planet: str = "FOO"
    requests_mock.get(
        ftx_fio.urls.localmarket_planet_url(planet=planet),
        status_code=200,
        json=valid_adlist,
    )

    data = ftx_fio.LocalMarket.planet(planet=planet)
    assert type(data) == LocalMarketAds
    assert len(data.BuyingAds) == 2
    assert len(data.SellingAds) == 1
    assert len(data.ShippingAds) == 1


def test_planet_type(requests_mock, ftx_fio: FIO, ad_1) -> None:
    planet: str = "FOO"
    requests_mock.get(
        ftx_fio.urls.localmarket_planet_type_url(planet=planet, adtype="BUY"),
        status_code=200,
        json=[ad_1],
    )

    (status, data) = ftx_fio.LocalMarket._planet_type(planet=planet, adtype="BUY")

    assert status == 200


def test_planet_buy(requests_mock, ftx_fio: FIO, ad_1) -> None:
    planet: str = "FOO"
    adtype: str = "BUY"

    requests_mock.get(
        ftx_fio.urls.localmarket_planet_type_url(planet=planet, adtype=adtype),
        status_code=200,
        json=[ad_1],
    )

    data = ftx_fio.LocalMarket.planet_buy(planet=planet)
    assert type(data) == LocalMarketAdList


def test_planet_buy_invalid(requests_mock, ftx_fio: FIO) -> None:
    planet: str = "FOO"
    adtype: str = "BUY"

    requests_mock.get(
        ftx_fio.urls.localmarket_planet_type_url(planet=planet, adtype=adtype),
        status_code=204,
    )

    with pytest.raises(PlanetOrAdsNotFound):
        ftx_fio.LocalMarket.planet_buy(planet=planet)


def test_planet_sell(requests_mock, ftx_fio: FIO, ad_1) -> None:
    planet: str = "FOO"
    adtype: str = "SELL"

    requests_mock.get(
        ftx_fio.urls.localmarket_planet_type_url(planet=planet, adtype=adtype),
        status_code=200,
        json=[ad_1],
    )

    data = ftx_fio.LocalMarket.planet_sell(planet=planet)
    assert type(data) == LocalMarketAdList


def test_planet_sell_invalid(requests_mock, ftx_fio: FIO) -> None:
    planet: str = "FOO"
    adtype: str = "SELL"

    requests_mock.get(
        ftx_fio.urls.localmarket_planet_type_url(planet=planet, adtype=adtype),
        status_code=204,
    )

    with pytest.raises(PlanetOrAdsNotFound):
        ftx_fio.LocalMarket.planet_sell(planet=planet)


def test_planet_shipping(requests_mock, ftx_fio: FIO, shipping_ad_1) -> None:
    planet: str = "FOO"
    adtype: str = "SHIP"

    requests_mock.get(
        ftx_fio.urls.localmarket_planet_type_url(planet=planet, adtype=adtype),
        status_code=200,
        json=[shipping_ad_1],
    )

    data = ftx_fio.LocalMarket.planet_shipping(planet=planet)
    assert type(data) == LocalMarketShippingAdList


def test_planet_shipping_invalid(requests_mock, ftx_fio: FIO) -> None:
    planet: str = "FOO"
    adtype: str = "SHIP"

    requests_mock.get(
        ftx_fio.urls.localmarket_planet_type_url(planet=planet, adtype=adtype),
        status_code=204,
    )

    with pytest.raises(PlanetOrAdsNotFound):
        ftx_fio.LocalMarket.planet_shipping(planet=planet)


def test_planet_shipping_from(requests_mock, ftx_fio: FIO, shipping_ad_1) -> None:
    planet: str = "FOO"

    requests_mock.get(
        ftx_fio.urls.localmarket_shipping_source_url(planet=planet),
        status_code=200,
        json=[shipping_ad_1],
    )

    data = ftx_fio.LocalMarket.shipping_from(planet=planet)
    assert type(data) == LocalMarketShippingAdList


def test_planet_shipping_from_invalid(requests_mock, ftx_fio: FIO) -> None:
    planet: str = "FOO"

    requests_mock.get(
        ftx_fio.urls.localmarket_shipping_source_url(planet=planet),
        status_code=204,
    )

    with pytest.raises(PlanetOrAdsNotFound):
        ftx_fio.LocalMarket.shipping_from(planet=planet)


def test_planet_shipping_to(requests_mock, ftx_fio: FIO, shipping_ad_1) -> None:
    planet: str = "FOO"

    requests_mock.get(
        ftx_fio.urls.localmarket_shipping_destination_url(planet=planet),
        status_code=200,
        json=[shipping_ad_1],
    )

    data = ftx_fio.LocalMarket.shipping_to(planet=planet)
    assert type(data) == LocalMarketShippingAdList


def test_planet_shipping_to_invalid(requests_mock, ftx_fio: FIO) -> None:
    planet: str = "FOO"

    requests_mock.get(
        ftx_fio.urls.localmarket_shipping_destination_url(planet=planet),
        status_code=204,
    )

    with pytest.raises(PlanetOrAdsNotFound):
        ftx_fio.LocalMarket.shipping_to(planet=planet)


def test_company_notfound(requests_mock, ftx_fio: FIO) -> None:
    company: str = "FOO"
    requests_mock.get(
        ftx_fio.urls.localmarket_company_url(companycode=company),
        status_code=204,
    )

    with pytest.raises(CompanyOrAdsNotFound):
        ftx_fio.LocalMarket.company(companycode=company)


def test_company_valid(requests_mock, ftx_fio: FIO, valid_adlist) -> None:
    company: str = "FOO"
    requests_mock.get(
        ftx_fio.urls.localmarket_company_url(companycode=company),
        status_code=200,
        json=valid_adlist,
    )

    data = ftx_fio.LocalMarket.company(companycode=company)
    assert type(data) == LocalMarketAds
    assert len(data.BuyingAds) == 2
    assert len(data.SellingAds) == 1
    assert len(data.ShippingAds) == 1
