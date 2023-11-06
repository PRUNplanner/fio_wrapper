import pytest
from fio_wrapper import FIO


@pytest.fixture()
def ftx_fio() -> FIO:
    return FIO()


@pytest.fixture()
def ftx_fio_key() -> FIO:
    return FIO(api_key="abc")
