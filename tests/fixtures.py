import pytest
from fio_wrapper import FIO


@pytest.fixture()
def ftx_fio() -> FIO:
    return FIO()
