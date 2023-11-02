import pytest
from pyfio import validate_localmarket_adtype
from pyfio.exceptions import InvalidAdType


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
