from typing import Dict
import pytest
from pyfio import (
    FIO,
    validate_exchange_code,
    validate_company_code,
    OrderList,
    Order,
    CompanyCodeInvalid,
    ExchangeTickerList,
    ExchangeTicker,
    ExchangeTickerFull,
    ExchangeTickerFullList,
    ExchangeTickerNotFound,
)


@pytest.fixture()
def ftx_fio() -> FIO:
    return FIO()


@pytest.fixture()
def order_1() -> Dict:
    return {"Ticker": "FF.AI1", "Buys": [{"Count": 9035, "Cost": 10.5}], "Sells": []}


@pytest.fixture()
def order_2() -> Dict:
    return {
        "Ticker": "SF.AI1",
        "Buys": [],
        "Sells": [{"Count": 43418, "Cost": 13.100000381469727}],
    }


@pytest.fixture()
def exchangeticker_1() -> Dict:
    return {
        "MaterialTicker": "AAR",
        "ExchangeCode": "AI1",
        "MMBuy": None,
        "MMSell": None,
        "PriceAverage": 14500.0,
        "AskCount": 8,
        "Ask": 14500.0,
        "Supply": 22,
        "BidCount": 35,
        "Bid": 14000.0,
        "Demand": 45,
    }


@pytest.fixture()
def exchangeticker_2() -> Dict:
    return {
        "MaterialTicker": "RAT",
        "ExchangeCode": "AI1",
        "MMBuy": 32.0,
        "MMSell": 166.0,
        "PriceAverage": 108.01,
        "AskCount": 194,
        "Ask": 93.0,
        "Supply": 185598,
        "BidCount": 1070,
        "Bid": 90.7,
        "Demand": 86058,
    }


@pytest.fixture()
def exchangeticker_full() -> Dict:
    return {
        "BuyingOrders": [
            {
                "OrderId": "ca5d3f26edee32dd099f89aac5884ae6",
                "CompanyId": "b4bed09f4edbfbd58cda37af268a17f0",
                "CompanyName": "Trakesa",
                "CompanyCode": "TRKS",
                "ItemCount": 200,
                "ItemCost": 200.0,
            },
            {
                "OrderId": "04d1417bed0d712db308c288e9fac516",
                "CompanyId": "9be31f83f9aff9f9f12d331853e15904",
                "CompanyName": "Circle_of_Life",
                "CompanyCode": "CIRC",
                "ItemCount": 50,
                "ItemCost": 50.0,
            },
            {
                "OrderId": "ed907d4b7d907b6d06562841390d7cbf",
                "CompanyId": "d2b11009b4d4d0f556e660ca8a54e638",
                "CompanyName": "Zen Interstellar Propellant",
                "CompanyCode": "ZIPP",
                "ItemCount": 211,
                "ItemCost": 100.0,
            },
        ],
        "SellingOrders": [
            {
                "OrderId": "e41a616bdd4930dcd63a7b6681b7d213",
                "CompanyId": "fcef882f0ed9aa6c5724f625edac0d15",
                "CompanyName": "Atomic Farms",
                "CompanyCode": "ATOM",
                "ItemCount": 1358,
                "ItemCost": 400.0,
            },
            {
                "OrderId": "15f77125d8f7708bf7e9f47b7753fe31",
                "CompanyId": "fcef882f0ed9aa6c5724f625edac0d15",
                "CompanyName": "Atomic Farms",
                "CompanyCode": "ATOM",
                "ItemCount": 3000,
                "ItemCost": 4500.0,
            },
            {
                "OrderId": "2e2b6a6a471c2e58bb18fc229b1eefbf",
                "CompanyId": "b684016c66d650417a7a81a980283602",
                "CompanyName": "Harvesters Combine",
                "CompanyCode": "HARC",
                "ItemCount": 114,
                "ItemCost": 5000.0,
            },
        ],
        "CXDataModelId": "0037f5f779eb63ac545af0d5c1744061",
        "MaterialName": "zircon",
        "MaterialTicker": "ZIR",
        "MaterialId": "82583e13472538b113667abc82421bda",
        "ExchangeName": "Moria Station Commodity Exchange",
        "ExchangeCode": "NC1",
        "Currency": "NCC",
        "Previous": None,
        "Price": 400.0,
        "PriceTimeEpochMs": 1698497241809,
        "High": 400.0,
        "AllTimeHigh": 4000.0,
        "Low": 300.0,
        "AllTimeLow": 29.299999237060547,
        "Ask": 400.0,
        "AskCount": 1358,
        "Bid": 200.0,
        "BidCount": 200,
        "Supply": 4472,
        "Demand": 461,
        "Traded": 2200,
        "VolumeAmount": 824200.0,
        "PriceAverage": 371.0299987792969,
        "NarrowPriceBandLow": 37.11000061035156,
        "NarrowPriceBandHigh": 927.5700073242188,
        "WidePriceBandLow": 37.11000061035156,
        "WidePriceBandHigh": 927.5700073242188,
        "MMBuy": None,
        "MMSell": None,
        "UserNameSubmitted": "BOBEMOR",
        "Timestamp": "2023-10-30T13:20:08.590949",
    }


def test_validate_company_code() -> None:
    with pytest.raises(CompanyCodeInvalid):
        validate_company_code("")

    with pytest.raises(CompanyCodeInvalid):
        validate_company_code("12345")


def test_OrderList_iter(order_1, order_2) -> None:
    data = OrderList.model_validate([order_1, order_2])

    for material in data:
        assert type(material) == Order


def test_ExchangeTickerList_iter(exchangeticker_1, exchangeticker_2) -> None:
    data = ExchangeTickerList.model_validate([exchangeticker_1, exchangeticker_2])

    for material in data:
        assert type(material) == ExchangeTicker


def test_ExchangeTickerFullList_iter(exchangeticker_full) -> None:
    data = ExchangeTickerFullList.model_validate(
        [exchangeticker_full, exchangeticker_full]
    )

    for material in data:
        assert type(material) == ExchangeTickerFull


def test_validate_exchange_code_none() -> None:
    from pyfio.exceptions import ExchangeTickerInvalid

    with pytest.raises(ExchangeTickerInvalid):
        validate_exchange_code(None)


def test_validate_exchangeticker(ftx_fio: FIO) -> None:
    from pyfio.exceptions import ExchangeTickerInvalid

    with pytest.raises(ExchangeTickerInvalid):
        ftx_fio.Exchange._validate_exchangeticker(None)

    with pytest.raises(ExchangeTickerInvalid):
        ftx_fio.Exchange._validate_exchangeticker("RAT.AI")

    with pytest.raises(ExchangeTickerInvalid):
        ftx_fio.Exchange._validate_exchangeticker("RATAI1")

    with pytest.raises(ExchangeTickerInvalid):
        ftx_fio.Exchange._validate_exchangeticker(".")

    with pytest.raises(ExchangeTickerInvalid):
        ftx_fio.Exchange._validate_exchangeticker(".AI1")

    with pytest.raises(ExchangeTickerInvalid):
        ftx_fio.Exchange._validate_exchangeticker("C.")

    with pytest.raises(ExchangeTickerInvalid):
        ftx_fio.Exchange._validate_exchangeticker("ABCD.")

    with pytest.raises(ExchangeTickerInvalid):
        ftx_fio.Exchange._validate_exchangeticker("RAT.AII")

    with pytest.raises(ExchangeTickerInvalid):
        ftx_fio.Exchange._validate_exchangeticker("RAT.AII1")


def test_exchange_get(requests_mock, exchangeticker_full, ftx_fio: FIO) -> None:
    requests_mock.get(
        ftx_fio._adapter.urls.exchange_get_url("AAR.AI1"),
        status_code=200,
        json=exchangeticker_full,
    )

    data = ftx_fio.Exchange.get("AAR.AI1")
    assert type(data) == ExchangeTickerFull


def test_exchange_get_notfound(requests_mock, ftx_fio: FIO) -> None:
    requests_mock.get(
        ftx_fio._adapter.urls.exchange_get_url("AAR.AI1"),
        status_code=204,
    )

    with pytest.raises(ExchangeTickerNotFound):
        ftx_fio.Exchange.get("AAR.AI1")


def test_exchange_all(
    requests_mock, exchangeticker_1, exchangeticker_2, ftx_fio: FIO
) -> None:
    requests_mock.get(
        ftx_fio._adapter.urls.exchange_get_all_url(),
        status_code=200,
        json=[exchangeticker_1, exchangeticker_2],
    )
    data = ftx_fio.Exchange.all()

    assert type(data) == ExchangeTickerList


def test_exchange_full(requests_mock, exchangeticker_full, ftx_fio: FIO) -> None:
    requests_mock.get(
        ftx_fio._adapter.urls.exchange_get_full_url(),
        status_code=200,
        json=[exchangeticker_full, exchangeticker_full],
    )
    data = ftx_fio.Exchange.full()

    assert type(data) == ExchangeTickerFullList


def test_get_orders(requests_mock, order_1, order_2, ftx_fio: FIO) -> None:
    with pytest.raises(CompanyCodeInvalid):
        ftx_fio.Exchange.get_orders(company_code="")

    company_code: str = "SKYP"

    requests_mock.get(
        ftx_fio._adapter.urls.exchange_get_orders_companycode(
            company_code=company_code
        ),
        status_code=200,
        json=[order_1, order_2],
    )

    data = ftx_fio.Exchange.get_orders(company_code=company_code)

    assert type(data) == OrderList


def test_get_orders_exchange(requests_mock, order_1, order_2, ftx_fio: FIO) -> None:
    company_code: str = "SKYP"
    exchange_code: str = "AI1"

    with pytest.raises(CompanyCodeInvalid):
        ftx_fio.Exchange.get_orders_exchange(company_code="", exchange_code="")

    requests_mock.get(
        ftx_fio._adapter.urls.exchange_get_orders_companycode_exchange(
            company_code=company_code, exchange_code=exchange_code
        ),
        status_code=200,
        json=[order_1, order_2],
    )

    data = ftx_fio.Exchange.get_orders_exchange(
        company_code=company_code, exchange_code=exchange_code
    )

    assert type(data) == OrderList
