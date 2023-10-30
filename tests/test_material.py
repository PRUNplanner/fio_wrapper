from typing import Dict
import pytest
from pyfio import FIO, MaterialModel, MaterialModelList


@pytest.fixture()
def ftx_fio() -> FIO:
    return FIO()


@pytest.fixture()
def material_1() -> Dict:
    return {
        "MaterialId": "4fca6f5b5e6c3b8a1b887c6dc99db146",
        "CategoryName": "consumables (basic)",
        "CategoryId": "3f047ec3043bdd795fd7272d6be98799",
        "Name": "drinkingWater",
        "Ticker": "DW",
        "Weight": 0.10000000149011612,
        "Volume": 0.10000000149011612,
        "UserNameSubmitted": "SAGANAKI",
        "Timestamp": "2023-10-28T19:26:21.831707",
    }


@pytest.fixture()
def material_2() -> Dict:
    return {
        "MaterialId": "ec6fe0efa83e52fd59f248a069aee9bb",
        "CategoryName": "agricultural products",
        "CategoryId": "510e7751c0eb6a51fd0fa73565365d1c",
        "Name": "proteinAlgae",
        "Ticker": "ALG",
        "Weight": 0.699999988079071,
        "Volume": 1.0,
        "UserNameSubmitted": "SAGANAKI",
        "Timestamp": "2023-10-28T19:26:21.831707",
    }


def test_validate_ticker(ftx_fio) -> None:
    from pyfio.exceptions import MaterialTickerInvalid

    with pytest.raises(MaterialTickerInvalid):
        ftx_fio.Material._validate_ticker(None)

    with pytest.raises(MaterialTickerInvalid):
        ftx_fio.Material._validate_ticker("1234")

    with pytest.raises(MaterialTickerInvalid):
        ftx_fio.Material._validate_ticker("D W")

    with pytest.raises(MaterialTickerInvalid):
        ftx_fio.Material._validate_ticker("")


def test_MaterialModelList_iter(material_1, material_2):
    data = MaterialModelList.model_validate([material_1, material_2])

    for material in data:
        assert type(material) == MaterialModel


def test_material_fail(requests_mock, ftx_fio: FIO) -> None:
    from pyfio.exceptions import MaterialTickerNotFound

    with pytest.raises(MaterialTickerNotFound):
        requests_mock.get(
            ftx_fio._adapter.urls.material_get_url("xyz"), status_code=204
        )
        ftx_fio.Material.get("xyz")


def test_material_single(requests_mock, material_1, ftx_fio: FIO) -> None:
    requests_mock.get(
        ftx_fio._adapter.urls.material_get_url("DW"),
        status_code=200,
        json=material_1,
    )
    data = ftx_fio.Material.get("DW")
    print(data)

    assert type(data) == MaterialModel
    assert data.Ticker == "DW"


def test_material_all(requests_mock, material_1, material_2, ftx_fio: FIO) -> None:
    requests_mock.get(
        ftx_fio._adapter.urls.material_allmaterials_url(),
        status_code=200,
        json=[material_1, material_2],
    )

    data = ftx_fio.Material.all()

    assert type(data) == MaterialModelList


def test_material_category(requests_mock, material_1, material_2, ftx_fio: FIO) -> None:
    category: str = "agricultural products"
    requests_mock.get(
        ftx_fio._adapter.urls.material_get_category(category_name=category),
        status_code=200,
        json=[material_1, material_2],
    )
    data = ftx_fio.Material.category(category_name=category)

    assert type(data) == MaterialModelList


def test_material_category_notfound(requests_mock, ftx_fio: FIO) -> None:
    from pyfio.exceptions import MaterialCategoryNotFound

    category: str = "xyz"
    requests_mock.get(
        ftx_fio._adapter.urls.material_get_category(category_name=category),
        status_code=204,
        json=[],
    )

    with pytest.raises(MaterialCategoryNotFound):
        data = ftx_fio.Material.category(category_name=category)


def test_material_category_empty(requests_mock, ftx_fio: FIO) -> None:
    from pyfio.exceptions import MaterialCategoryNotFound

    category: str = "xyz"
    requests_mock.get(
        ftx_fio._adapter.urls.material_get_category(category_name=category),
        status_code=200,
        json=[],
    )

    with pytest.raises(MaterialCategoryNotFound):
        data = ftx_fio.Material.category(category_name=category)
