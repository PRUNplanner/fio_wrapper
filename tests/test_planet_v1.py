from typing import Dict
import pytest
from pyfio import (
    FIO,
    Planet,
    PlanetList,
    PlanetFull,
    PlanetFullList,
    PlanetSite,
    PlanetSiteList,
)
from pyfio.exceptions import PlanetNotFound


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
                "MaterialId": "ec8dbb1d3f51d89c61b6f58fdd64a7f0",
                "ResourceType": "LIQUID",
                "Factor": 0.10999999940395355,
            },
            {
                "MaterialId": "6e16dbf050b98d9c4fc9c615b3367a0f",
                "ResourceType": "GASEOUS",
                "Factor": 0.17000000178813934,
            },
            {
                "MaterialId": "1f9a0293d9ba9bf519f71432e695edeb",
                "ResourceType": "MINERAL",
                "Factor": 0.28999999165534973,
            },
            {
                "MaterialId": "b9640b0d66e7d0ca7e4d3132711c97fc",
                "ResourceType": "MINERAL",
                "Factor": 0.20999999344348907,
            },
        ],
        "BuildRequirements": [
            {
                "MaterialName": "lightweightStructuralElements",
                "MaterialId": "8d4e0986419d2769fe50ac6497be6b7e",
                "MaterialTicker": "LSE",
                "MaterialCategory": "ef423f673d9e8c82043b4c5c63f6b55e",
                "MaterialAmount": 4,
                "MaterialWeight": 0.30000001192092896,
                "MaterialVolume": 1.2000000476837158,
            },
            {
                "MaterialName": "truss",
                "MaterialId": "ec53c7423b75ca0d868f9580ae921561",
                "MaterialTicker": "TRU",
                "MaterialCategory": "f8aebc7dd84ce14fae131aa0203d4498",
                "MaterialAmount": 8,
                "MaterialWeight": 0.10000000149011612,
                "MaterialVolume": 1.5,
            },
            {
                "MaterialName": "largePlasticsBoard",
                "MaterialId": "db4fbfd5c434a3952e7e1d37ae36158f",
                "MaterialTicker": "PSL",
                "MaterialCategory": "6316282906a9f68b0c7bb4396a26aa95",
                "MaterialAmount": 12,
                "MaterialWeight": 0.07999999821186066,
                "MaterialVolume": 0.800000011920929,
            },
            {
                "MaterialName": "lightweightDeckElements",
                "MaterialId": "3010d90fde69729f4754b092fdcda826",
                "MaterialTicker": "LDE",
                "MaterialCategory": "ef423f673d9e8c82043b4c5c63f6b55e",
                "MaterialAmount": 4,
                "MaterialWeight": 0.10000000149011612,
                "MaterialVolume": 1.2000000476837158,
            },
            {
                "MaterialName": "lightweightWindow",
                "MaterialId": "b29a0e901300857a8672f0643f7d796a",
                "MaterialTicker": "LTA",
                "MaterialCategory": "ef423f673d9e8c82043b4c5c63f6b55e",
                "MaterialAmount": 4,
                "MaterialWeight": 0.30000001192092896,
                "MaterialVolume": 0.5,
            },
            {
                "MaterialName": "mineralConstructionGranulate",
                "MaterialId": "cc5fb1618f0506e80bfbcee9ae2605ab",
                "MaterialTicker": "MCG",
                "MaterialCategory": "156bbcce730fba6169338d560f05fd26",
                "MaterialAmount": 100,
                "MaterialWeight": 0.23999999463558197,
                "MaterialVolume": 0.10000000149011612,
            },
        ],
        "ProductionFees": [
            {
                "Category": "AGRICULTURE",
                "WorkforceLevel": "SCIENTIST",
                "FeeAmount": 1980,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "FUEL_REFINING",
                "WorkforceLevel": "ENGINEER",
                "FeeAmount": 1080,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "FUEL_REFINING",
                "WorkforceLevel": "SCIENTIST",
                "FeeAmount": 1980,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "MANUFACTURING",
                "WorkforceLevel": "PIONEER",
                "FeeAmount": 43,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "MANUFACTURING",
                "WorkforceLevel": "SETTLER",
                "FeeAmount": 43,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "MANUFACTURING",
                "WorkforceLevel": "TECHNICIAN",
                "FeeAmount": 270,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "MANUFACTURING",
                "WorkforceLevel": "ENGINEER",
                "FeeAmount": 1080,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "MANUFACTURING",
                "WorkforceLevel": "SCIENTIST",
                "FeeAmount": 1980,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "METALLURGY",
                "WorkforceLevel": "PIONEER",
                "FeeAmount": 43,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "METALLURGY",
                "WorkforceLevel": "SETTLER",
                "FeeAmount": 43,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "METALLURGY",
                "WorkforceLevel": "TECHNICIAN",
                "FeeAmount": 270,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "METALLURGY",
                "WorkforceLevel": "ENGINEER",
                "FeeAmount": 1080,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "METALLURGY",
                "WorkforceLevel": "SCIENTIST",
                "FeeAmount": 1980,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "RESOURCE_EXTRACTION",
                "WorkforceLevel": "PIONEER",
                "FeeAmount": 43,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "RESOURCE_EXTRACTION",
                "WorkforceLevel": "SETTLER",
                "FeeAmount": 43,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "RESOURCE_EXTRACTION",
                "WorkforceLevel": "TECHNICIAN",
                "FeeAmount": 270,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "RESOURCE_EXTRACTION",
                "WorkforceLevel": "ENGINEER",
                "FeeAmount": 1080,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "RESOURCE_EXTRACTION",
                "WorkforceLevel": "SCIENTIST",
                "FeeAmount": 1980,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "AGRICULTURE",
                "WorkforceLevel": "SETTLER",
                "FeeAmount": 43,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "AGRICULTURE",
                "WorkforceLevel": "PIONEER",
                "FeeAmount": 43,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "FUEL_REFINING",
                "WorkforceLevel": "TECHNICIAN",
                "FeeAmount": 270,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "AGRICULTURE",
                "WorkforceLevel": "ENGINEER",
                "FeeAmount": 1080,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "FUEL_REFINING",
                "WorkforceLevel": "SETTLER",
                "FeeAmount": 43,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "FOOD_INDUSTRIES",
                "WorkforceLevel": "SCIENTIST",
                "FeeAmount": 1980,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "CHEMISTRY",
                "WorkforceLevel": "PIONEER",
                "FeeAmount": 55,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "CHEMISTRY",
                "WorkforceLevel": "SETTLER",
                "FeeAmount": 55,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "CHEMISTRY",
                "WorkforceLevel": "TECHNICIAN",
                "FeeAmount": 270,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "CHEMISTRY",
                "WorkforceLevel": "ENGINEER",
                "FeeAmount": 1080,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "CHEMISTRY",
                "WorkforceLevel": "SCIENTIST",
                "FeeAmount": 1980,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "CONSTRUCTION",
                "WorkforceLevel": "PIONEER",
                "FeeAmount": 43,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "CONSTRUCTION",
                "WorkforceLevel": "SETTLER",
                "FeeAmount": 43,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "CONSTRUCTION",
                "WorkforceLevel": "TECHNICIAN",
                "FeeAmount": 270,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "CONSTRUCTION",
                "WorkforceLevel": "ENGINEER",
                "FeeAmount": 1080,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "CONSTRUCTION",
                "WorkforceLevel": "SCIENTIST",
                "FeeAmount": 1980,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "ELECTRONICS",
                "WorkforceLevel": "PIONEER",
                "FeeAmount": 43,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "ELECTRONICS",
                "WorkforceLevel": "SETTLER",
                "FeeAmount": 43,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "ELECTRONICS",
                "WorkforceLevel": "TECHNICIAN",
                "FeeAmount": 270,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "ELECTRONICS",
                "WorkforceLevel": "ENGINEER",
                "FeeAmount": 1080,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "ELECTRONICS",
                "WorkforceLevel": "SCIENTIST",
                "FeeAmount": 1980,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "FOOD_INDUSTRIES",
                "WorkforceLevel": "PIONEER",
                "FeeAmount": 43,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "AGRICULTURE",
                "WorkforceLevel": "TECHNICIAN",
                "FeeAmount": 270,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "FOOD_INDUSTRIES",
                "WorkforceLevel": "TECHNICIAN",
                "FeeAmount": 270,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "FOOD_INDUSTRIES",
                "WorkforceLevel": "ENGINEER",
                "FeeAmount": 1080,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "FUEL_REFINING",
                "WorkforceLevel": "PIONEER",
                "FeeAmount": 43,
                "FeeCurrency": "NCC",
            },
            {
                "Category": "FOOD_INDUSTRIES",
                "WorkforceLevel": "SETTLER",
                "FeeAmount": 43,
                "FeeCurrency": "NCC",
            },
        ],
        "COGCPrograms": [
            {
                "ProgramType": "ADVERTISING_CHEMISTRY",
                "StartEpochMs": 1698863376669,
                "EndEpochMs": 1699468176669,
            },
            {
                "ProgramType": "ADVERTISING_CHEMISTRY",
                "StartEpochMs": 1693420176669,
                "EndEpochMs": 1694024976669,
            },
            {
                "ProgramType": "ADVERTISING_CHEMISTRY",
                "StartEpochMs": 1698258576669,
                "EndEpochMs": 1698863376669,
            },
            {
                "ProgramType": "ADVERTISING_CHEMISTRY",
                "StartEpochMs": 1697653776669,
                "EndEpochMs": 1698258576669,
            },
            {
                "ProgramType": "ADVERTISING_CHEMISTRY",
                "StartEpochMs": 1697048976669,
                "EndEpochMs": 1697653776669,
            },
            {
                "ProgramType": "ADVERTISING_CHEMISTRY",
                "StartEpochMs": 1696444176669,
                "EndEpochMs": 1697048976669,
            },
            {
                "ProgramType": "ADVERTISING_CHEMISTRY",
                "StartEpochMs": 1695839376669,
                "EndEpochMs": 1696444176669,
            },
            {
                "ProgramType": "ADVERTISING_CHEMISTRY",
                "StartEpochMs": 1695234576669,
                "EndEpochMs": 1695839376669,
            },
            {
                "ProgramType": "ADVERTISING_CHEMISTRY",
                "StartEpochMs": 1694629776669,
                "EndEpochMs": 1695234576669,
            },
            {
                "ProgramType": "ADVERTISING_CHEMISTRY",
                "StartEpochMs": 1694024976669,
                "EndEpochMs": 1694629776669,
            },
        ],
        "COGCVotes": [
            {
                "CompanyName": "SpectrumSupplies",
                "CompanyCode": "SMSS",
                "Influence": 1800,
                "VoteType": "WORKFORCE_PIONEERS",
                "VoteTimeEpochMs": 1698496827276,
            },
            {
                "CompanyName": "Citrus Export Syndicate",
                "CompanyCode": "LYME",
                "Influence": 1175,
                "VoteType": "ADVERTISING_CHEMISTRY",
                "VoteTimeEpochMs": 1698258583932,
            },
            {
                "CompanyName": "Cypher Industries",
                "CompanyCode": "CYPH",
                "Influence": 2660,
                "VoteType": "WORKFORCE_PIONEERS",
                "VoteTimeEpochMs": 1698258592451,
            },
            {
                "CompanyName": "KB Industries",
                "CompanyCode": "KBI",
                "Influence": 1560,
                "VoteType": "ADVERTISING_CHEMISTRY",
                "VoteTimeEpochMs": 1698258642937,
            },
            {
                "CompanyName": "King Victualler",
                "CompanyCode": "KKV",
                "Influence": 2378.75,
                "VoteType": "ADVERTISING_CHEMISTRY",
                "VoteTimeEpochMs": 1698258728183,
            },
            {
                "CompanyName": "Highlander",
                "CompanyCode": "HGH",
                "Influence": 1109.25,
                "VoteType": "ADVERTISING_CHEMISTRY",
                "VoteTimeEpochMs": 1698258893360,
            },
            {
                "CompanyName": "Tinker Industries",
                "CompanyCode": "TIN",
                "Influence": 1287.5,
                "VoteType": "ADVERTISING_CHEMISTRY",
                "VoteTimeEpochMs": 1698258974694,
            },
            {
                "CompanyName": "Copious Ore and Kabobs",
                "CompanyCode": "COK",
                "Influence": 1526.25,
                "VoteType": "ADVERTISING_CHEMISTRY",
                "VoteTimeEpochMs": 1698258982077,
            },
            {
                "CompanyName": "Rexus",
                "CompanyCode": "REXX",
                "Influence": 2043.75,
                "VoteType": "ADVERTISING_CHEMISTRY",
                "VoteTimeEpochMs": 1698259359537,
            },
            {
                "CompanyName": "Portgas",
                "CompanyCode": "POGA",
                "Influence": 1937.5,
                "VoteType": "ADVERTISING_CHEMISTRY",
                "VoteTimeEpochMs": 1698259856364,
            },
            {
                "CompanyName": "Lumber Liquidators",
                "CompanyCode": "BMEX",
                "Influence": 1308.75,
                "VoteType": "ADVERTISING_CHEMISTRY",
                "VoteTimeEpochMs": 1698549400005,
            },
            {
                "CompanyName": "BlackGuard",
                "CompanyCode": "BG",
                "Influence": 1210,
                "VoteType": "ADVERTISING_CHEMISTRY",
                "VoteTimeEpochMs": 1698260129804,
            },
            {
                "CompanyName": "Nosirrath",
                "CompanyCode": "NOS",
                "Influence": 1742.5,
                "VoteType": "ADVERTISING_CHEMISTRY",
                "VoteTimeEpochMs": 1698260828767,
            },
            {
                "CompanyName": "East India Space Company",
                "CompanyCode": "EISC",
                "Influence": 3600,
                "VoteType": "WORKFORCE_PIONEERS",
                "VoteTimeEpochMs": 1698260889724,
            },
            {
                "CompanyName": "Nanny Co-op",
                "CompanyCode": "NNY",
                "Influence": 1680,
                "VoteType": "ADVERTISING_CHEMISTRY",
                "VoteTimeEpochMs": 1698261324311,
            },
            {
                "CompanyName": "LavAzza",
                "CompanyCode": "LAVA",
                "Influence": 1345,
                "VoteType": "ADVERTISING_CHEMISTRY",
                "VoteTimeEpochMs": 1698261736114,
            },
            {
                "CompanyName": "Lumerz LLP",
                "CompanyCode": "LUME",
                "Influence": 1447.5,
                "VoteType": "ADVERTISING_CHEMISTRY",
                "VoteTimeEpochMs": 1698273248488,
            },
            {
                "CompanyName": "Nth Metal",
                "CompanyCode": "NTH",
                "Influence": 1135,
                "VoteType": "ADVERTISING_CHEMISTRY",
                "VoteTimeEpochMs": 1698277336087,
            },
            {
                "CompanyName": "Amp Partners",
                "CompanyCode": "AMP",
                "Influence": 2368.75,
                "VoteType": "ADVERTISING_CHEMISTRY",
                "VoteTimeEpochMs": 1698288361647,
            },
            {
                "CompanyName": "Steelwing Hydrotechnical",
                "CompanyCode": "SWHY",
                "Influence": 1280,
                "VoteType": "ADVERTISING_CHEMISTRY",
                "VoteTimeEpochMs": 1698314954316,
            },
            {
                "CompanyName": "Infernal Foundaries",
                "CompanyCode": "IFRN",
                "Influence": 760,
                "VoteType": "WORKFORCE_PIONEERS",
                "VoteTimeEpochMs": 1698350987777,
            },
            {
                "CompanyName": "Skyprod",
                "CompanyCode": "SKYP",
                "Influence": 1782.5,
                "VoteType": "ADVERTISING_CHEMISTRY",
                "VoteTimeEpochMs": 1698260471995,
            },
            {
                "CompanyName": "Bizotic",
                "CompanyCode": "BZT",
                "Influence": 1436.25,
                "VoteType": "ADVERTISING_CHEMISTRY",
                "VoteTimeEpochMs": 1698651904545,
            },
        ],
        "COGCUpkeep": [],
        "PlanetId": "7f1135f5d7792a058c8be66e7cbcb536",
        "PlanetNaturalId": "OT-580b",
        "PlanetName": "Montem",
        "Namer": None,
        "NamingDataEpochMs": 0,
        "Nameable": False,
        "SystemId": "49b6615d39ccba05752b3be77b2ebf36",
        "Gravity": 0.922335147857666,
        "MagneticField": 0.7182995080947876,
        "Mass": 7.797300945837227e24,
        "MassEarth": 1.3056432008743286,
        "OrbitSemiMajorAxis": 139417977000,
        "OrbitEccentricity": 0.03147958219051361,
        "OrbitInclination": 0.04501096159219742,
        "OrbitRightAscension": 0,
        "OrbitPeriapsis": 0,
        "OrbitIndex": 2,
        "Pressure": 0.9165661931037903,
        "Radiation": 1.4921821515009263e-23,
        "Radius": 7584996.5,
        "Sunlight": 1621.1890869140625,
        "Surface": True,
        "Temperature": 3.772547960281372,
        "Fertility": -0.19999998807907104,
        "HasLocalMarket": True,
        "HasChamberOfCommerce": True,
        "HasWarehouse": True,
        "HasAdministrationCenter": True,
        "HasShipyard": False,
        "FactionCode": "NC",
        "FactionName": "NEO Charter Exploration",
        "GovernorId": "5ceba0296b7aa04fb0dbf704c3be3d42",
        "GovernorUserName": "DogeConomy",
        "GovernorCorporationId": "2ed91b7077fd578a6552b48d2b3a95fc",
        "GovernorCorporationName": "Rubicate's Montem Govmt V2.0",
        "GovernorCorporationCode": "RMG2",
        "CurrencyName": "NCE Coupons",
        "CurrencyCode": "NCC",
        "CollectorId": "2ed91b7077fd578a6552b48d2b3a95fc",
        "CollectorName": "Rubicate's Montem Govmt V2.0",
        "CollectorCode": "RMG2",
        "BaseLocalMarketFee": 0,
        "LocalMarketFeeFactor": 3,
        "WarehouseFee": 100,
        "PopulationId": "a6f1ef590c2110aa3195e97ef931d122",
        "COGCProgramStatus": "ACTIVE",
        "PlanetTier": 0,
        "UserNameSubmitted": "STRAKE",
        "Timestamp": "2023-07-15T00:21:41.935321",
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

    requests_mock.get(ftx_fio._adapter.urls.planet_get_url(planet), status_code=204)

    with pytest.raises(PlanetNotFound):
        ftx_fio.Planet.get(planet=planet)


def test_planet_get(requests_mock, ftx_fio: FIO, planet_full_1) -> None:
    planet: str = "FOO"

    requests_mock.get(
        ftx_fio._adapter.urls.planet_get_url(planet),
        status_code=200,
        json=planet_full_1,
    )

    data = ftx_fio.Planet.get(planet=planet)
    assert type(data) == PlanetFull


def test_planet_all(requests_mock, ftx_fio: FIO, planet_1) -> None:
    requests_mock.get(ftx_fio._adapter.urls.planet_all_url(), json=[planet_1, planet_1])

    data = ftx_fio.Planet.all()
    for planet in data:
        assert type(planet) == Planet


def test_planet_full(requests_mock, ftx_fio: FIO, planet_full_1) -> None:
    requests_mock.get(
        ftx_fio._adapter.urls.planet_full_url(), json=[planet_full_1, planet_full_1]
    )

    data = ftx_fio.Planet.full()
    for planet in data:
        assert type(planet) == PlanetFull


def test_planet_sites_notfound(requests_mock, ftx_fio: FIO) -> None:
    planet: str = "FOO"

    requests_mock.get(ftx_fio._adapter.urls.planet_sites_url(planet), status_code=204)

    with pytest.raises(PlanetNotFound):
        ftx_fio.Planet.sites(planet=planet)


def test_planet_sites(requests_mock, ftx_fio: FIO, planet_site_1) -> None:
    planet: str = "FOO"

    requests_mock.get(
        ftx_fio._adapter.urls.planet_sites_url(planet),
        status_code=200,
        json=[planet_site_1, planet_site_1],
    )

    data = ftx_fio.Planet.sites(planet=planet)
    for site in data:
        assert type(site) == PlanetSite
