from typing import List
from pydantic import BaseModel, RootModel, Field, NaiveDatetime


class MaterialModel(BaseModel):
    MaterialId: str = Field(min_length=32)
    CategoryName: str
    CategoryId: str = Field(min_length=32)
    Name: str
    Ticker: str
    Weight: int | float
    Volume: int | float
    UserNameSubmitted: str
    Timestamp: NaiveDatetime


class MaterialModelList(RootModel):
    root: List[MaterialModel]

    def __iter__(self):
        return iter(self.root)
