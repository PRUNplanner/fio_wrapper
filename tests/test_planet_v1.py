from typing import Dict
import pytest
from fio_wrapper import (
    FIO,
    Planet,
    PlanetList,
    PlanetFull,
    PlanetFullList,
    PlanetSite,
    PlanetSiteList,
)
from fio_wrapper.exceptions import (
    PlanetNotFound,
    PlanetSearchDistanceChecksInvalid,
    PlanetSearchInvalidRequest,
    PlanetSearchMaterialsInvalid,
)


@pytest.fixture()
def ftx_fio() -> FIO:
    return FIO()


@pytest.fixture()
def planet_1() -> Dict:
    return {"PlanetNaturalId": "CH-771c", "PlanetName": "CH-771c"}


@pytest.fixture()
def planet_full_1() -> Dict:
    return {
        "Resources": [
            {
                "MaterialId": "bcf4a2029e461cf76d29de8c66ec2ff9",
                "ResourceType": "GASEOUS",
                "Factor": 0.10999999940395355
            },
            {
                "MaterialId": "ec8dbb1d3f51d89c61b6f58fdd64a7f0",
                "ResourceType": "LIQUID",
                "Factor": 0.20999999344348907
            },
            {
                "MaterialId": "6e16dbf050b98d9c4fc9c615b3367a0f",
                "ResourceType": "GASEOUS",
                "Factor": 0.2800000011920929
            },
            {
                "MaterialId": "c5236c5b79b9e75ddbce16887aeda338",
                "ResourceType": "MINERAL",
                "Factor": 0.23000000417232513
            }
        ],
        "BuildRequirements": [
            {
                "MaterialName": "lightweightStructuralElements",
                "MaterialId": "8d4e0986419d2769fe50ac6497be6b7e",
                "MaterialTicker": "LSE",
                "MaterialCategory": "ef423f673d9e8c82043b4c5c63f6b55e",
                "MaterialAmount": 4,
                "MaterialWeight": 0.30000001192092896,
                "MaterialVolume": 1.2000000476837158
            },
            {
                "MaterialName": "truss",
                "MaterialId": "ec53c7423b75ca0d868f9580ae921561",
                "MaterialTicker": "TRU",
                "MaterialCategory": "f8aebc7dd84ce14fae131aa0203d4498",
                "MaterialAmount": 8,
                "MaterialWeight": 0.10000000149011612,
                "MaterialVolume": 1.5
            },
            {
                "MaterialName": "largePlasticsBoard",
                "MaterialId": "db4fbfd5c434a3952e7e1d37ae36158f",
                "MaterialTicker": "PSL",
                "MaterialCategory": "6316282906a9f68b0c7bb4396a26aa95",
                "MaterialAmount": 12,
                "MaterialWeight": 0.07999999821186066,
                "MaterialVolume": 0.800000011920929
            },
            {
                "MaterialName": "lightweightDeckElements",
                "MaterialId": "3010d90fde69729f4754b092fdcda826",
                "MaterialTicker": "LDE",
                "MaterialCategory": "ef423f673d9e8c82043b4c5c63f6b55e",
                "MaterialAmount": 4,
                "MaterialWeight": 0.10000000149011612,
                "MaterialVolume": 1.2000000476837158
            },
            {
                "MaterialName": "lightweightWindow",
                "MaterialId": "b29a0e901300857a8672f0643f7d796a",
                "MaterialTicker": "LTA",
                "MaterialCategory": "ef423f673d9e8c82043b4c5c63f6b55e",
                "MaterialAmount": 4,
                "MaterialWeight": 0.30000001192092896,
                "MaterialVolume": 0.5
            },
            {
                "MaterialName": "mineralConstructionGranulate",
                "MaterialId": "cc5fb1618f0506e80bfbcee9ae2605ab",
                "MaterialTicker": "MCG",
                "MaterialCategory": "156bbcce730fba6169338d560f05fd26",
                "MaterialAmount": 100,
                "MaterialWeight": 0.23999999463558197,
                "MaterialVolume": 0.10000000149011612
            }
        ],
        "ProductionFees": [
            {
                "Category": "AGRICULTURE",
                "WorkforceLevel": "SCIENTIST",
                "FeeAmount": 10.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "FUEL_REFINING",
                "WorkforceLevel": "ENGINEER",
                "FeeAmount": 10.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "FUEL_REFINING",
                "WorkforceLevel": "SCIENTIST",
                "FeeAmount": 10.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "MANUFACTURING",
                "WorkforceLevel": "PIONEER",
                "FeeAmount": 30.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "MANUFACTURING",
                "WorkforceLevel": "SETTLER",
                "FeeAmount": 120.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "MANUFACTURING",
                "WorkforceLevel": "TECHNICIAN",
                "FeeAmount": 270.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "MANUFACTURING",
                "WorkforceLevel": "ENGINEER",
                "FeeAmount": 1080.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "MANUFACTURING",
                "WorkforceLevel": "SCIENTIST",
                "FeeAmount": 1980.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "METALLURGY",
                "WorkforceLevel": "PIONEER",
                "FeeAmount": 20.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "METALLURGY",
                "WorkforceLevel": "SETTLER",
                "FeeAmount": 80.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "METALLURGY",
                "WorkforceLevel": "TECHNICIAN",
                "FeeAmount": 240.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "METALLURGY",
                "WorkforceLevel": "ENGINEER",
                "FeeAmount": 1000.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "METALLURGY",
                "WorkforceLevel": "SCIENTIST",
                "FeeAmount": 10.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "RESOURCE_EXTRACTION",
                "WorkforceLevel": "PIONEER",
                "FeeAmount": 10.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "RESOURCE_EXTRACTION",
                "WorkforceLevel": "SETTLER",
                "FeeAmount": 10.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "RESOURCE_EXTRACTION",
                "WorkforceLevel": "TECHNICIAN",
                "FeeAmount": 10.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "RESOURCE_EXTRACTION",
                "WorkforceLevel": "ENGINEER",
                "FeeAmount": 10.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "RESOURCE_EXTRACTION",
                "WorkforceLevel": "SCIENTIST",
                "FeeAmount": 10.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "AGRICULTURE",
                "WorkforceLevel": "SETTLER",
                "FeeAmount": 80.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "AGRICULTURE",
                "WorkforceLevel": "PIONEER",
                "FeeAmount": 20.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "FUEL_REFINING",
                "WorkforceLevel": "TECHNICIAN",
                "FeeAmount": 10.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "AGRICULTURE",
                "WorkforceLevel": "ENGINEER",
                "FeeAmount": 10.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "FUEL_REFINING",
                "WorkforceLevel": "SETTLER",
                "FeeAmount": 10.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "FOOD_INDUSTRIES",
                "WorkforceLevel": "SCIENTIST",
                "FeeAmount": 10.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "CHEMISTRY",
                "WorkforceLevel": "PIONEER",
                "FeeAmount": 20.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "CHEMISTRY",
                "WorkforceLevel": "SETTLER",
                "FeeAmount": 80.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "CHEMISTRY",
                "WorkforceLevel": "TECHNICIAN",
                "FeeAmount": 240.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "CHEMISTRY",
                "WorkforceLevel": "ENGINEER",
                "FeeAmount": 1000.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "CHEMISTRY",
                "WorkforceLevel": "SCIENTIST",
                "FeeAmount": 1980.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "CONSTRUCTION",
                "WorkforceLevel": "PIONEER",
                "FeeAmount": 20.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "CONSTRUCTION",
                "WorkforceLevel": "SETTLER",
                "FeeAmount": 80.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "CONSTRUCTION",
                "WorkforceLevel": "TECHNICIAN",
                "FeeAmount": 240.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "CONSTRUCTION",
                "WorkforceLevel": "ENGINEER",
                "FeeAmount": 1000.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "CONSTRUCTION",
                "WorkforceLevel": "SCIENTIST",
                "FeeAmount": 10.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "ELECTRONICS",
                "WorkforceLevel": "PIONEER",
                "FeeAmount": 20.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "ELECTRONICS",
                "WorkforceLevel": "SETTLER",
                "FeeAmount": 80.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "ELECTRONICS",
                "WorkforceLevel": "TECHNICIAN",
                "FeeAmount": 240.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "ELECTRONICS",
                "WorkforceLevel": "ENGINEER",
                "FeeAmount": 1080.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "ELECTRONICS",
                "WorkforceLevel": "SCIENTIST",
                "FeeAmount": 1980.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "FOOD_INDUSTRIES",
                "WorkforceLevel": "PIONEER",
                "FeeAmount": 20.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "AGRICULTURE",
                "WorkforceLevel": "TECHNICIAN",
                "FeeAmount": 240.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "FOOD_INDUSTRIES",
                "WorkforceLevel": "TECHNICIAN",
                "FeeAmount": 240.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "FOOD_INDUSTRIES",
                "WorkforceLevel": "ENGINEER",
                "FeeAmount": 10.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "FUEL_REFINING",
                "WorkforceLevel": "PIONEER",
                "FeeAmount": 10.0,
                "FeeCurrency": "CIS"
            },
            {
                "Category": "FOOD_INDUSTRIES",
                "WorkforceLevel": "SETTLER",
                "FeeAmount": 80.0,
                "FeeCurrency": "CIS"
            }
        ],
        "COGCPrograms": [
            {
                "ProgramType": "ADVERTISING_MANUFACTURING",
                "StartEpochMs": 1745168530311,
                "EndEpochMs": 1745773330311
            },
            {
                "ProgramType": "ADVERTISING_MANUFACTURING",
                "StartEpochMs": 1740934930311,
                "EndEpochMs": 1741539730311
            },
            {
                "ProgramType": "ADVERTISING_MANUFACTURING",
                "StartEpochMs": 1739725330311,
                "EndEpochMs": 1740330130311
            },
            {
                "ProgramType": "ADVERTISING_MANUFACTURING",
                "StartEpochMs": 1740330130311,
                "EndEpochMs": 1740934930311
            },
            {
                "ProgramType": "ADVERTISING_MANUFACTURING",
                "StartEpochMs": 1743958930311,
                "EndEpochMs": 1744563730311
            },
            {
                "ProgramType": "ADVERTISING_MANUFACTURING",
                "StartEpochMs": 1743354130311,
                "EndEpochMs": 1743958930311
            },
            {
                "ProgramType": "ADVERTISING_MANUFACTURING",
                "StartEpochMs": 1744563730311,
                "EndEpochMs": 1745168530311
            },
            {
                "ProgramType": "ADVERTISING_MANUFACTURING",
                "StartEpochMs": 1741539730311,
                "EndEpochMs": 1742144530311
            },
            {
                "ProgramType": "ADVERTISING_MANUFACTURING",
                "StartEpochMs": 1742144530311,
                "EndEpochMs": 1742749330311
            },
            {
                "ProgramType": "ADVERTISING_MANUFACTURING",
                "StartEpochMs": 1742749330311,
                "EndEpochMs": 1743354130311
            }
        ],
        "COGCVotes": [
            {
                "CompanyName": "NIKNIK's Co",
                "CompanyCode": "NIK",
                "Influence": 580.0,
                "VoteType": "ADVERTISING_FUEL_REFINING",
                "VoteTimeEpochMs": 1744659692143
            },
            {
                "CompanyName": "Food'R'Us",
                "CompanyCode": "FRS",
                "Influence": 1252.5,
                "VoteType": "ADVERTISING_MANUFACTURING",
                "VoteTimeEpochMs": 1744564075651
            },
            {
                "CompanyName": "FaLLen Corp",
                "CompanyCode": "FALL",
                "Influence": 650.0,
                "VoteType": "ADVERTISING_MANUFACTURING",
                "VoteTimeEpochMs": 1744566039083
            },
            {
                "CompanyName": "Androidica Intergalactic",
                "CompanyCode": "PC7",
                "Influence": 3408.75,
                "VoteType": "ADVERTISING_MANUFACTURING",
                "VoteTimeEpochMs": 1744566415817
            },
            {
                "CompanyName": "SUPERBAD VENTURES",
                "CompanyCode": "EZ",
                "Influence": 762.5,
                "VoteType": "ADVERTISING_MANUFACTURING",
                "VoteTimeEpochMs": 1744772298420
            },
            {
                "CompanyName": "OmniFuel",
                "CompanyCode": "OMNF",
                "Influence": 195.0,
                "VoteType": "ADVERTISING_FUEL_REFINING",
                "VoteTimeEpochMs": 1744771628656
            },
            {
                "CompanyName": "InterStellaTrucking",
                "CompanyCode": "IST",
                "Influence": 525.0,
                "VoteType": "ADVERTISING_MANUFACTURING",
                "VoteTimeEpochMs": 1744940893909
            },
            {
                "CompanyName": "Industry Cubed",
                "CompanyCode": "III",
                "Influence": 380.0,
                "VoteType": "ADVERTISING_MANUFACTURING",
                "VoteTimeEpochMs": 1744890639597
            },
            {
                "CompanyName": "Endurance",
                "CompanyCode": "ED24",
                "Influence": 2000.0,
                "VoteType": "ADVERTISING_MANUFACTURING",
                "VoteTimeEpochMs": 1744563747393
            },
            {
                "CompanyName": "KB Industries (liquidated)",
                "CompanyCode": None,
                "Influence": 800.0,
                "VoteType": "ADVERTISING_ELECTRONICS",
                "VoteTimeEpochMs": 1743887753138
            }
        ],
        "COGCUpkeep": [],
        "PlanetId": "a09f3bf153025929b2fb266e4119931a",
        "PlanetNaturalId": "UV-351a",
        "PlanetName": "Katoa",
        "Namer": None,
        "NamingDataEpochMs": 0,
        "Nameable": False,
        "SystemId": "92029ff27c1abe932bd2c61ee4c492c7",
        "Gravity": 0.9244412779808044,
        "MagneticField": 0.6173155903816223,
        "Mass": 5.658493204210973E+24,
        "MassEarth": 0.947503924369812,
        "OrbitSemiMajorAxis": 249802440000.0,
        "OrbitEccentricity": 0.04760166257619858,
        "OrbitInclination": -0.04166974499821663,
        "OrbitRightAscension": 0.0,
        "OrbitPeriapsis": 0.0,
        "OrbitIndex": 3,
        "Pressure": 1.04933762550354,
        "Radiation": 6.345644847682585E-24,
        "Radius": 6454139.5,
        "Sunlight": 507.498046875,
        "Surface": True,
        "Temperature": 11.877347946166992,
        "Fertility": -0.1600000262260437,
        "HasLocalMarket": True,
        "HasChamberOfCommerce": True,
        "HasWarehouse": True,
        "HasAdministrationCenter": True,
        "HasShipyard": False,
        "FactionCode": "CI",
        "FactionName": "Castillo-Ito Mercantile",
        "GoverningEntity": "99aca2be2d2e47be5585f63e7c17ea26",
        "CurrencyName": "Sol",
        "CurrencyCode": "CIS",
        "BaseLocalMarketFee": 0.0,
        "LocalMarketFeeFactor": 5.0,
        "WarehouseFee": 100.0,
        "EstablishmentFee": 0.0,
        "PopulationId": "d1c90d1c7d92931bfcea1a4dda0fe33c",
        "COGCProgramStatus": "ACTIVE",
        "PlanetTier": 0,
        "UserNameSubmitted": "LEGUVAN",
        "Timestamp": "2024-09-10T15:37:42.141591"
    }


@pytest.fixture()
def planet_site_1() -> Dict:
    return {
        "PlanetId": "7f1135f5d7792a058c8be66e7cbcb536",
        "OwnerId": "bc73d0bc32c540f393248f70231150b9",
        "OwnerName": "Skyprod",
        "OwnerCode": "SKYP",
        "PlotNumber": 157,
        "PlotId": "d45320db099700d9aa8b99ca252a8830",
        "SiteId": "d45320db",
    }


# Model
def test_model_PlanetList(planet_1) -> None:
    data = PlanetList.model_validate([planet_1, planet_1])

    for planet in data:
        assert type(planet) == Planet


def test_model_PlanetFullList(planet_full_1) -> None:
    data = PlanetFullList.model_validate([planet_full_1, planet_full_1])

    for planet in data:
        assert type(planet) == PlanetFull


def test_model_PlanetSiteList(planet_site_1) -> None:
    data = PlanetSiteList.model_validate([planet_site_1, planet_site_1])

    for site in data:
        assert type(site) == PlanetSite


# Endpoints


def test_planet_get_notfound(requests_mock, ftx_fio: FIO) -> None:
    planet: str = "FOO"

    requests_mock.get(ftx_fio.urls.planet_get_url(planet), status_code=204)

    with pytest.raises(PlanetNotFound):
        ftx_fio.Planet.get(planet=planet)


def test_planet_get(requests_mock, ftx_fio: FIO, planet_full_1) -> None:
    planet: str = "FOO"

    requests_mock.get(
        ftx_fio.urls.planet_get_url(planet),
        status_code=200,
        json=planet_full_1,
    )

    data = ftx_fio.Planet.get(planet=planet)
    assert type(data) == PlanetFull


def test_planet_all(requests_mock, ftx_fio: FIO, planet_1) -> None:
    requests_mock.get(ftx_fio.urls.planet_all_url(), json=[planet_1, planet_1])

    data = ftx_fio.Planet.all()
    for planet in data:
        assert type(planet) == Planet


def test_planet_full(requests_mock, ftx_fio: FIO, planet_full_1) -> None:
    requests_mock.get(
        ftx_fio.urls.planet_full_url(), json=[planet_full_1, planet_full_1]
    )

    data = ftx_fio.Planet.full()
    for planet in data:
        assert type(planet) == PlanetFull


def test_planet_sites_notfound(requests_mock, ftx_fio: FIO) -> None:
    planet: str = "FOO"

    requests_mock.get(ftx_fio.urls.planet_sites_url(planet), status_code=204)

    with pytest.raises(PlanetNotFound):
        ftx_fio.Planet.sites(planet=planet)


def test_planet_sites(requests_mock, ftx_fio: FIO, planet_site_1) -> None:
    planet: str = "FOO"

    requests_mock.get(
        ftx_fio.urls.planet_sites_url(planet),
        status_code=200,
        json=[planet_site_1, planet_site_1],
    )

    data = ftx_fio.Planet.sites(planet=planet)
    for site in data:
        assert type(site) == PlanetSite


def test_planet_search_invalid_material(ftx_fio: FIO) -> None:
    with pytest.raises(PlanetSearchMaterialsInvalid):
        ftx_fio.Planet.search(materials=[1, 2, 3])


def test_planet_search_invalid_distances(ftx_fio: FIO) -> None:
    with pytest.raises(PlanetSearchDistanceChecksInvalid):
        ftx_fio.Planet.search(distance_checks=[1, 2, 3])


def test_planet_search(requests_mock, ftx_fio: FIO, planet_full_1) -> None:
    requests_mock.post(
        ftx_fio.urls.planet_search_url(),
        status_code=200,
        json=[planet_full_1, planet_full_1],
    )

    data = ftx_fio.Planet.search()

    assert type(data) == PlanetFullList


def test_planet_search_invalid(requests_mock, ftx_fio: FIO) -> None:
    requests_mock.post(
        ftx_fio.urls.planet_search_url(),
        status_code=400,
    )

    with pytest.raises(PlanetSearchInvalidRequest):
        ftx_fio.Planet.search()
