from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, RootModel, Field, NaiveDatetime


class ExchangeOrder(BaseModel):
    OrderId: str = Field(min_length=32)
    CompanyId: str = Field(min_length=32)
    CompanyName: str
    CompanyCode: str
    ItemCount: Optional[int]  # Market Maker ItemCount = null
    ItemCost: float


class ExchangeTicker(BaseModel):
    BuyingOrders: Optional[List[ExchangeOrder]]
    SellingOrders: Optional[List[ExchangeOrder]]

    CXDataModelId: str = Field(min_length=32)
    MaterialName: str
    MaterialTicker: str = Field(max_length=3)
    MaterialId: str = Field(min_length=32)
    ExchangeName: str
    ExchangeCode: str = Field(min_length=3)
    Currency: str = Field(min_length=2)
    Price: float
    PriceTimeEpochMs: datetime
    High: float
    AllTimeHigh: float
    Low: float
    AllTimeLow: float
    Ask: float
    AskCount: int
    Bid: float
    BidCount: int
    Supply: int
    Demand: int
    Traded: int
    VolumeAmount: float
    PriceAverage: float
    NarrowPriceBandLow: float
    NarrowPriceBandHigh: float
    WidePriceBandLow: float
    WidePriceBandHigh: float
    MMBuy: float
    MMSell: float
    UserNameSubmitted: str
    Timestamp: NaiveDatetime


class OrderDefinition(BaseModel):
    Count: int
    Cost: float


class Order(BaseModel):
    Ticker: str = Field(max_length=7)
    Buys: Optional[List[OrderDefinition]]
    Sells: Optional[List[OrderDefinition]]


class OrderList(RootModel):
    root: List[Order]

    def __iter__(self):
        return iter(self.root)
