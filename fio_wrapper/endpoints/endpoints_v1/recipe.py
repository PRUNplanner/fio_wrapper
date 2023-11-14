"""Access recipe information from FIO.
"""
from typing import Optional
from fio_wrapper.endpoints.abstracts.abstract_endpoint import AbstractEndpoint
from fio_wrapper.endpoints.abstracts.abstract_recipe import AbstractRecipe
from fio_wrapper.models.recipe_models import MaterialRecipeList, RecipeList


class Recipe(AbstractRecipe, AbstractEndpoint):
    # /recipes/{Ticker}
    def get(
        self, material_ticker: str, timeout: Optional[float] = None
    ) -> MaterialRecipeList:
        """Gets all recipes for given material from FIO

        Args:
            material_ticker (str): Material Ticker (e.g. "FE")
            timeout (float, optional): Request timeout in seconds. Defaults to None.

        Returns:
            MaterialRecipeList: List of Recipes as List[MaterialRecipeList]
        """
        (_, data) = self.adapter.get(
            endpoint=self.urls.recipe_get_url(material_ticker=material_ticker),
            timeout=timeout,
        )

        return MaterialRecipeList.model_validate(data)

    # /recipes/allrecipes
    def all(self, timeout: Optional[float] = None) -> RecipeList:
        """Gets all recipes from FIO

        Args:
            timeout (float, optional): Request timeout in seconds. Defaults to None.

        Returns:
            RecipeList: List of Recipes as List[RecipeList]
        """
        (_, data) = self.adapter.get(
            endpoint=self.urls.recipe_get_all_url(), timeout=timeout
        )

        return RecipeList.model_validate(data)
