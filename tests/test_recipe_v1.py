from typing import Dict
import pytest
from fio_wrapper import FIO, Recipe, RecipeList, MaterialRecipe, MaterialRecipeList


from .fixtures import ftx_fio


@pytest.fixture()
def recipe_1() -> Dict:
    return {
        "BuildingTicker": "TNP",
        "RecipeName": "1xTC 4xREA 4xFLX=>1xETC",
        "StandardRecipeName": "TNP:4xFLX-4xREA-1xTC=>1xETC",
        "Inputs": [
            {"Ticker": "FLX", "Amount": 4},
            {"Ticker": "TC", "Amount": 1},
            {"Ticker": "REA", "Amount": 4},
        ],
        "Outputs": [{"Ticker": "ETC", "Amount": 1}],
        "TimeMs": 69120000,
    }


@pytest.fixture()
def material_recipe_1() -> Dict:
    return {
        "BuildingTicker": "FS",
        "BuildingRecipeId": None,
        "Inputs": [
            {
                "CommodityName": "aluminium",
                "CommodityTicker": "AL",
                "Weight": 2.700000047683716,
                "Volume": 1.0,
                "Amount": 10,
            },
            {
                "CommodityName": "steel",
                "CommodityTicker": "STL",
                "Weight": 7.849999904632568,
                "Volume": 1.0,
                "Amount": 4,
            },
        ],
        "Outputs": [
            {
                "CommodityName": "floatingTank",
                "CommodityTicker": "FLO",
                "Weight": 1.0,
                "Volume": 2.0,
                "Amount": 1,
            }
        ],
        "DurationMs": 69120000,
        "RecipeName": "10xAL 4xSTL=>1xFLO",
        "StandardRecipeName": None,
    }


# Model
def test_RecipeList(recipe_1) -> None:
    data = RecipeList.model_validate([recipe_1, recipe_1])

    for recipe in data:
        assert type(recipe) == Recipe


def test_MaterialRecipeList(material_recipe_1) -> None:
    data = MaterialRecipeList.model_validate([material_recipe_1, material_recipe_1])

    for material_recipe in data:
        assert type(material_recipe) == MaterialRecipe


# Endpoints


def test_recipe_get(requests_mock, ftx_fio: FIO, material_recipe_1) -> None:
    material_ticker: str = "AL"
    requests_mock.get(
        ftx_fio._adapter.urls.recipe_get_url(material_ticker=material_ticker),
        status_code=200,
        json=[material_recipe_1],
    )

    data = ftx_fio.Recipe.get(material_ticker=material_ticker)
    assert type(data) == MaterialRecipeList


def test_recipe_all(requests_mock, ftx_fio: FIO, recipe_1) -> None:
    requests_mock.get(
        ftx_fio._adapter.urls.recipe_get_all_url(),
        status_code=200,
        json=[recipe_1, recipe_1],
    )

    data = ftx_fio.Recipe.all()
    for recipe in data:
        assert type(recipe) == Recipe
