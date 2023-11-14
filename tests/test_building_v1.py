from typing import Dict
import pytest
from fio_wrapper import FIO, BuildingTicker, BuildingTickerList
from fio_wrapper.exceptions import BuildingTickerNotFound


@pytest.fixture()
def ftx_fio() -> FIO:
    return FIO()


@pytest.fixture()
def building_1() -> Dict:
    return {
        "BuildingCosts": [
            {
                "CommodityName": "basicStructuralElements",
                "CommodityTicker": "BSE",
                "Weight": 0.30000001192092896,
                "Volume": 0.5,
                "Amount": 12,
            }
        ],
        "Recipes": [
            {
                "Inputs": [],
                "Outputs": [],
                "BuildingRecipeId": "@RIG=>",
                "DurationMs": 17280000,
                "RecipeName": "=>",
                "StandardRecipeName": "RIG:=>",
            }
        ],
        "BuildingId": "00e3d3d9ac2fc9ba7cac62519915dc43",
        "Name": "rig",
        "Ticker": "RIG",
        "Expertise": "RESOURCE_EXTRACTION",
        "Pioneers": 30,
        "Settlers": 0,
        "Technicians": 0,
        "Engineers": 0,
        "Scientists": 0,
        "AreaCost": 10,
        "UserNameSubmitted": "SAGANAKI",
        "Timestamp": "2023-08-31T01:16:36.359921",
    }


@pytest.fixture()
def building_2() -> Dict:
    return {
        "BuildingCosts": [
            {
                "CommodityName": "lightweightDeckElements",
                "CommodityTicker": "LDE",
                "Weight": 0.10000000149011612,
                "Volume": 1.2000000476837158,
                "Amount": 8,
            },
            {
                "CommodityName": "lightweightStructuralElements",
                "CommodityTicker": "LSE",
                "Weight": 0.30000001192092896,
                "Volume": 1.2000000476837158,
                "Amount": 12,
            },
            {
                "CommodityName": "truss",
                "CommodityTicker": "TRU",
                "Weight": 0.10000000149011612,
                "Volume": 1.5,
                "Amount": 8,
            },
            {
                "CommodityName": "lightweightBulkhead",
                "CommodityTicker": "LBH",
                "Weight": 0.20000000298023224,
                "Volume": 0.6000000238418579,
                "Amount": 6,
            },
        ],
        "Recipes": [
            {
                "Inputs": [
                    {
                        "CommodityName": "flux",
                        "CommodityTicker": "FLX",
                        "Weight": 0.25,
                        "Volume": 0.10000000149011612,
                        "Amount": 4,
                    },
                    {
                        "CommodityName": "technetium",
                        "CommodityTicker": "TC",
                        "Weight": 11.800000190734863,
                        "Volume": 1.0,
                        "Amount": 1,
                    },
                    {
                        "CommodityName": "chemicalReagents",
                        "CommodityTicker": "REA",
                        "Weight": 0.05000000074505806,
                        "Volume": 0.05000000074505806,
                        "Amount": 4,
                    },
                ],
                "Outputs": [
                    {
                        "CommodityName": "enrichedTechnetium",
                        "CommodityTicker": "ETC",
                        "Weight": 4.099999904632568,
                        "Volume": 1.0,
                        "Amount": 1,
                    }
                ],
                "BuildingRecipeId": "1xTC 4xREA 4xFLX@TNP=>1xETC",
                "DurationMs": 69120000,
                "RecipeName": "1xTC 4xREA 4xFLX=>1xETC",
                "StandardRecipeName": "TNP:4xFLX-4xREA-1xTC=>1xETC",
            },
            {
                "Inputs": [
                    {
                        "CommodityName": "technetiumOxide",
                        "CommodityTicker": "TCO",
                        "Weight": 9.800000190734863,
                        "Volume": 1.0,
                        "Amount": 1,
                    }
                ],
                "Outputs": [
                    {
                        "CommodityName": "technetium",
                        "CommodityTicker": "TC",
                        "Weight": 11.800000190734863,
                        "Volume": 1.0,
                        "Amount": 1,
                    },
                    {
                        "CommodityName": "oxygen",
                        "CommodityTicker": "O",
                        "Weight": 1.1410000324249268,
                        "Volume": 1.0,
                        "Amount": 1,
                    },
                ],
                "BuildingRecipeId": "1xTCO@TNP=>1xTC 1xO",
                "DurationMs": 58752000,
                "RecipeName": "1xTCO=>1xTC 1xO",
                "StandardRecipeName": "TNP:1xTCO=>1xO-1xTC",
            },
            {
                "Inputs": [
                    {
                        "CommodityName": "technetium",
                        "CommodityTicker": "TC",
                        "Weight": 11.800000190734863,
                        "Volume": 1.0,
                        "Amount": 1,
                    }
                ],
                "Outputs": [
                    {
                        "CommodityName": "technetiumStabilizers",
                        "CommodityTicker": "TCS",
                        "Weight": 3.4000000953674316,
                        "Volume": 1.2000000476837158,
                        "Amount": 3,
                    }
                ],
                "BuildingRecipeId": "1xTC@TNP=>3xTCS",
                "DurationMs": 43200000,
                "RecipeName": "1xTC=>3xTCS",
                "StandardRecipeName": "TNP:1xTC=>3xTCS",
            },
        ],
        "BuildingId": "0473a002be6c4feb92433cc819e10b5d",
        "Name": "technetiumProcessing",
        "Ticker": "TNP",
        "Expertise": "CHEMISTRY",
        "Pioneers": 0,
        "Settlers": 0,
        "Technicians": 80,
        "Engineers": 0,
        "Scientists": 0,
        "AreaCost": 30,
        "UserNameSubmitted": "JELUTZ77",
        "Timestamp": "2023-10-22T02:32:23.971976",
    }


# Model


def test_BuildingTickerList(building_1, building_2) -> None:
    data = BuildingTickerList.model_validate([building_1, building_2])

    for building in data:
        assert type(building) == BuildingTicker


# Endpoints


def test_building_get_notfound(requests_mock, ftx_fio: FIO) -> None:
    building_ticker: str = "FOO"
    requests_mock.get(
        ftx_fio.urls.building_get_url(building_ticker=building_ticker),
        status_code=204,
    )
    with pytest.raises(BuildingTickerNotFound):
        ftx_fio.Building.get(building_ticker=building_ticker)


def test_building_get(requests_mock, ftx_fio: FIO, building_1) -> None:
    building_ticker: str = "RIG"
    requests_mock.get(
        ftx_fio.urls.building_get_url(building_ticker=building_ticker),
        status_code=200,
        json=building_1,
    )

    data = ftx_fio.Building.get(building_ticker=building_ticker)
    assert type(data) == BuildingTicker
    assert data.Ticker == building_ticker


def test_building_all(requests_mock, ftx_fio: FIO, building_1, building_2) -> None:
    requests_mock.get(
        ftx_fio.urls.building_get_all_url(),
        status_code=200,
        json=[building_1, building_2],
    )

    data = ftx_fio.Building.all()

    for building in data:
        assert type(building) == BuildingTicker
