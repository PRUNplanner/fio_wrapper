import pytest
from pyfio import FIO


@pytest.fixture()
def ftx_fio() -> FIO:
    return FIO()
