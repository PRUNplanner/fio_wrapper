from typing import List
from pydantic import BaseModel, RootModel, Field, NaiveDatetime


class MaterialTicker(BaseModel):
    MaterialId: str = Field(min_length=32)
    CategoryName: str
    CategoryId: str = Field(min_length=32)
    Name: str
    Ticker: str
    Weight: float
    Volume: float
    UserNameSubmitted: str
    Timestamp: NaiveDatetime


class MaterialTickerList(RootModel):
    root: List[MaterialTicker]

    def __iter__(self):
        return iter(self.root)
