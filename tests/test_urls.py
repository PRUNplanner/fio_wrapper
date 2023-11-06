import pytest
from fio_wrapper import URLs


@pytest.fixture
def url() -> URLs:
    return URLs(base_url="foo")


def test_url_base(url: URLs) -> None:
    assert url.base_url == "foo"


# Material


def test_material_url(url: URLs) -> None:
    assert url.material_url() == "foo/material"


# Exchange


def test_exchange_get_url(url: URLs) -> None:
    assert url.exchange_get_url("AI1") == "foo/exchange/AI1"


def test_exchange_get_orders_companycode(url: URLs) -> None:
    assert url.exchange_get_orders_companycode("SKYP") == "foo/exchange/orders/SKYP"


def test_exchange_get_orders_companycode_exchange(url: URLs) -> None:
    assert (
        url.exchange_get_orders_companycode_exchange(
            company_code="SKYP", exchange_code="AI1"
        )
        == "foo/exchange/orders/SKYP/AI1"
    )


def test_exchange_get_all_url(url: URLs) -> None:
    assert url.exchange_get_all_url() == "foo/exchange/all"


def test_exchange_get_full_url(url: URLs) -> None:
    assert url.exchange_get_full_url() == "foo/exchange/full"


# Building


def test_building_url(url: URLs) -> None:
    assert url.building_url() == "foo/building"


def test_building_get_url(url: URLs) -> None:
    assert url.building_get_url(building_ticker="FOO") == "foo/building/FOO"


def test_building_get_all_url(url: URLs) -> None:
    assert url.building_get_all_url() == "foo/building/allbuildings"


# Recipe


def test_recipe_url(url: URLs) -> None:
    assert url.recipe_url() == "foo/recipes"


def test_recipe_get_url(url: URLs) -> None:
    assert url.recipe_get_url(material_ticker="FOO") == "foo/recipes/FOO"


def test_recipe_get_all_url(url: URLs) -> None:
    assert url.recipe_get_all_url() == "foo/recipes/allrecipes"


# Planet


def test_planet_url(url: URLs) -> None:
    assert url.planet_url() == "foo/planet"


def test_planet_get_url(url: URLs) -> None:
    assert url.planet_get_url(planet="moo") == "foo/planet/moo"


def test_planet_all_url(url: URLs) -> None:
    assert url.planet_all_url() == "foo/planet/allplanets"


def test_planet_full_url(url: URLs) -> None:
    assert url.planet_full_url() == "foo/planet/allplanets/full"


def test_planet_sites_url(url: URLs) -> None:
    assert url.planet_sites_url(planet="moo") == "foo/planet/sites/moo"


def test_planet_search_url(url: URLs) -> None:
    assert url.planet_search_url() == "foo/planet/search"


# LocalMarket


def test_localmarket_url(url: URLs) -> None:
    assert url.localmarket_url() == "foo/localmarket"


def test_localmarket_planet_url(url: URLs) -> None:
    assert url.localmarket_planet_url(planet="moo") == "foo/localmarket/planet/moo"


def test_localmarket_planet_type_url(url: URLs) -> None:
    assert (
        url.localmarket_planet_type_url(planet="moo", adtype="BUY")
        == "foo/localmarket/planet/moo/BUY"
    )


def test_localmarket_shipping_source_url(url: URLs) -> None:
    assert (
        url.localmarket_shipping_source_url(planet="moo")
        == "foo/localmarket/shipping/source/moo"
    )


def test_localmarket_shipping_destination_url(url: URLs) -> None:
    assert (
        url.localmarket_shipping_destination_url(planet="moo")
        == "foo/localmarket/shipping/destination/moo"
    )


def test_localmarket_company_url(url: URLs) -> None:
    assert (
        url.localmarket_company_url(companycode="moo") == "foo/localmarket/company/moo"
    )


# Sites


def test_sites_planets_get_url(url: URLs) -> None:
    assert url.sites_planets_get_url(username="moo") == "foo/sites/planets/moo"


def test_sites_planets_get_planet_url(url: URLs) -> None:
    assert (
        url.sites_planets_get_planet_url(username="moo", planet="foo")
        == "foo/sites/moo/foo"
    )


def test_sites_warehouses_get(url: URLs) -> None:
    assert url.sites_warehouses_get(username="moo") == "foo/sites/warehouses/moo"
