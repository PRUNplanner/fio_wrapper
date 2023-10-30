import pytest
from pyfio.endpoints.abstracts.abstract_building import AbstractBuilding
from pyfio.endpoints.abstracts.abstract_material import AbstractMaterial
from pyfio.endpoints.abstracts.abstract_exchange import AbstractExchange


@pytest.fixture()
def ab() -> AbstractBuilding:
    return AbstractBuilding()


@pytest.fixture()
def am() -> AbstractMaterial:
    return AbstractMaterial()


@pytest.fixture()
def ae() -> AbstractExchange:
    return AbstractExchange()


# Building
def test_abstract_building_get(ab: AbstractBuilding) -> None:
    with pytest.raises(NotImplementedError):
        ab.get(building_ticker="foo")


def test_abstract_building_allbuildings(ab: AbstractBuilding) -> None:
    with pytest.raises(NotImplementedError):
        ab.allbuildings()


# Material
def test_abstract_material_get(am: AbstractMaterial) -> None:
    with pytest.raises(NotImplementedError):
        am.get(material_ticker="foo")


def test_abstract_material_all(am: AbstractMaterial) -> None:
    with pytest.raises(NotImplementedError):
        am.all()


def test_abstract_material_category(am: AbstractMaterial) -> None:
    with pytest.raises(NotImplementedError):
        am.category(category_name="moo")


# Exchange
def test_abstract_exchange_get(ae: AbstractExchange) -> None:
    with pytest.raises(NotImplementedError):
        ae.get(exchange_ticker="moo")


def test_abstract_exchange_get_all(ae: AbstractExchange) -> None:
    with pytest.raises(NotImplementedError):
        ae.get_all()


def test_abstract_exchange_get_full(ae: AbstractExchange) -> None:
    with pytest.raises(NotImplementedError):
        ae.get_full()


def test_abstract_exchange_get_orders(ae: AbstractExchange) -> None:
    with pytest.raises(NotImplementedError):
        ae.get_orders(company_code="moo")


def test_abstract_exchange_get_orders_exchange(ae: AbstractExchange) -> None:
    with pytest.raises(NotImplementedError):
        ae.get_orders_exchange(company_code="foo", exchange_code="moo")
