"""Access recipe information from FIO.
"""
from fio_wrapper.endpoints.abstracts.abstract_recipe import AbstractRecipe
from fio_wrapper.fio_adapter import FIOAdapter
from fio_wrapper.models.recipe_models import MaterialRecipeList, RecipeList


class Recipe(AbstractRecipe):
    def __init__(self, adapter: FIOAdapter) -> None:
        self._adapter: FIOAdapter = adapter

    # /recipes/{Ticker}
    def get(self, material_ticker: str) -> MaterialRecipeList:
        """Gets all recipes for given material from FIO

        Args:
            material_ticker (str): Material Ticker (e.g. "FE")

        Returns:
            MaterialRecipeList: List of Recipes as List[MaterialRecipeList]
        """
        (_, data) = self._adapter.get(
            endpoint=self._adapter.urls.recipe_get_url(material_ticker=material_ticker)
        )

        return MaterialRecipeList.model_validate(data)

    # /recipes/allrecipes
    def all(self) -> RecipeList:
        """Gets all recipes from FIO

        Returns:
            RecipeList: List of Recipes as List[RecipeList]
        """
        (_, data) = self._adapter.get(endpoint=self._adapter.urls.recipe_get_all_url())

        return RecipeList.model_validate(data)
