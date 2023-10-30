from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, RootModel, Field, NaiveDatetime

# Exchange


class ExchangeOrder(BaseModel):
    OrderId: str = Field(min_length=32)
    CompanyId: str = Field(min_length=32)
    CompanyName: Optional[str]
    CompanyCode: Optional[str]
    ItemCount: Optional[int]  # Market Maker ItemCount = null
    ItemCost: float


class ExchangeTicker(BaseModel):
    MaterialTicker: str = Field(max_length=3)
    ExchangeCode: str = Field(min_length=3)
    MMBuy: Optional[float]
    MMSell: Optional[float]
    PriceAverage: Optional[float]
    Ask: Optional[float]
    AskCount: Optional[int]
    Bid: Optional[float]
    BidCount: Optional[int]
    Supply: Optional[int]
    Demand: Optional[int]


class ExchangeTickerList(RootModel):
    root: List[ExchangeTicker]

    def __iter__(self):
        return iter(self.root)


class ExchangeTickerFull(ExchangeTicker):
    BuyingOrders: Optional[List[ExchangeOrder]]
    SellingOrders: Optional[List[ExchangeOrder]]

    ExchangeName: str
    CXDataModelId: str = Field(min_length=32)
    MaterialName: str
    MaterialId: str = Field(min_length=32)
    Currency: str = Field(min_length=2)
    Price: Optional[float]
    PriceTimeEpochMs: Optional[datetime]
    High: Optional[float]
    AllTimeHigh: Optional[float]
    Low: Optional[float]
    AllTimeLow: Optional[float]
    Traded: Optional[int]
    VolumeAmount: Optional[float]
    NarrowPriceBandLow: Optional[float]
    NarrowPriceBandHigh: Optional[float]
    WidePriceBandLow: Optional[float]
    WidePriceBandHigh: Optional[float]
    UserNameSubmitted: str
    Timestamp: NaiveDatetime


class ExchangeTickerFullList(RootModel):
    root: List[ExchangeTickerFull]

    def __iter__(self):
        return iter(self.root)


# Order


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
