from typing import Optional, List
from pydantic import BaseModel, RootModel, Field
from datetime import datetime


class AdBase(BaseModel):
    ContractNaturalId: int
    PlanetId: str = Field(min_length=32)
    PlanetNaturalId: str
    PlanetName: str
    CreatorCompanyId: str = Field(min_length=32)
    CreatorCompanyName: str
    CreatorCompanyCode: str
    DeliveryTime: int
    CreationTimeEpochMs: datetime
    ExpiryTimeEpochMs: datetime
    MinimumRating: str


class Ad(AdBase):
    MaterialId: str = Field(min_length=32)
    MaterialName: str
    MaterialTicker: str
    MaterialCategory: str = Field(min_length=32)
    MaterialWeight: float
    MaterialVolume: float
    MaterialAmount: int
    Price: float
    PriceCurrency: str


class ShippingAd(AdBase):
    OriginPlanetId: str = Field(min_length=32)
    OriginPlanetNaturalId: str
    OriginPlanetName: str
    DestinationPlanetId: str = Field(min_length=32)
    DestinationPlanetNaturalId: str
    DestinationPlanetName: str
    CargoWeight: float
    CargoVolume: float
    PayoutPrice: int
    PayoutCurrency: str


class LocalMarketAds(BaseModel):
    BuyingAds: List[Ad]
    SellingAds: List[Ad]
    ShippingAds: List[ShippingAd]


class LocalMarketAdList(RootModel):
    root: List[Ad]

    def __iter__(self):
        return iter(self.root)


class LocalMarketShippingAdList(RootModel):
    root: List[ShippingAd]

    def __iter__(self):
        return iter(self.root)
