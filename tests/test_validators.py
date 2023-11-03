import pytest
from fio_wrapper import validate_localmarket_adtype
from fio_wrapper.exceptions import InvalidAdType
from fio_wrapper.validators import (
    validate_planet_search_distance_checks,
    validate_planet_search_materials,
)


def test_validate_localmarket_adtype() -> None:
    pass


@pytest.mark.parametrize(
    "inp", ["BUY", "BUYS", "BUYING", "SELL", "SELLS", "SELLING", "SHIP", "SHIPPING"]
)
def test_localmarket_adtype_valid(inp):
    try:
        validate_localmarket_adtype(adtype=inp)
    except InvalidAdType:
        pytest.fail("InvalidAdType")


@pytest.mark.parametrize("inp", ["", None, "foo"])
def test_localmarket_adtype_invalid(inp):
    with pytest.raises(InvalidAdType):
        validate_localmarket_adtype(adtype=inp)


@pytest.mark.parametrize(
    "input, expected",
    [
        ([], True),
        (["LST"], True),
        (["LST", "FEO", "H2O"], True),
        (None, False),
        (["LST", "FEO", ""], False),
        (["LST", "FEO", "toolong"], False),
        (["1", "2", "3", "4", "5"], False),
    ],
)
def test_validate_planet_search_materials(input, expected) -> None:
    assert validate_planet_search_materials(materials=input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ([], True),
        (["1", "2", "3"], True),
        (["1", "2", "3", "4"], False),
        (None, False),
    ],
)
def test_validate_planet_search_distance_checks(input, expected) -> None:
    assert validate_planet_search_distance_checks(distance_checks=input) == expected
