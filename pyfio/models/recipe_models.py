from typing import List, Optional
from pydantic import BaseModel, RootModel, Field, NaiveDatetime


class RecipeIO(BaseModel):
    Ticker: str = Field(max_length=3)
    Amount: int


class Recipe(BaseModel):
    Inputs: List[RecipeIO]
    Outputs: List[RecipeIO]

    BuildingTicker: str
    RecipeName: str
    StandardRecipeName: str

    TimeMs: int


class RecipeList(RootModel):
    root: List[Recipe]

    def __iter__(self):
        return iter(self.root)


class MaterialRecipeIO(BaseModel):
    CommodityName: str
    CommodityTicker: str = Field(max_length=3)
    Weight: float
    Volume: float
    Amount: int


class MaterialRecipe(BaseModel):
    BuildingTicker: str = Field(max_length=3)
    BuildingRecipeId: Optional[str]

    Inputs: List[MaterialRecipeIO]
    Outputs: List[MaterialRecipeIO]


class MaterialRecipeList(RootModel):
    root: List[MaterialRecipe]

    def __iter__(self):
        return iter(self.root)
