import pytest
from pyfio import FIO, validate_exchange_code


@pytest.fixture()
def ftx_fio() -> FIO:
    return FIO()


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
