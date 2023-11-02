from typing import List, Optional
from pydantic import BaseModel, RootModel, Field, NaiveDatetime


class BuildingRecipeIO(BaseModel):
    CommodityName: str
    CommodityTicker: str = Field(max_length=3)
    Weight: float
    Volume: float
    Amount: int


class BuildingRecipe(BaseModel):
    Inputs: List[BuildingRecipeIO]
    Outputs: List[BuildingRecipeIO]

    BuildingRecipeId: str
    RecipeName: str
    StandardRecipeName: str

    DurationMs: int


class BuildingCost(BaseModel):
    CommodityName: str
    CommodityTicker: str = Field(max_length=3)
    Weight: float
    Volume: float
    Amount: int


class BuildingTicker(BaseModel):
    Recipes: Optional[List[BuildingRecipe]]
    BuildingId: str = Field(min_length=32)
    Name: str
    Ticker: str = Field(max_length=3)
    Expertise: Optional[str]
    Pioneers: int
    Settlers: int
    Technicians: int
    Engineers: int
    Scientists: int
    AreaCost: int
    UserNameSubmitted: str
    Timestamp: NaiveDatetime


class BuildingTickerList(RootModel):
    root: List[BuildingTicker]

    def __iter__(self):
        return iter(self.root)
