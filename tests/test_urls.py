import pytest
from pyfio import URLs


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
