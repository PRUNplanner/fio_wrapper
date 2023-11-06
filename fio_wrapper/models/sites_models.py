from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, RootModel, Field, NaiveDatetime


class SiteBuildingMaterial(BaseModel):
    MaterialId: str = Field(min_length=32)
    MaterialName: str
    MaterialTicker: str = Field(max_length=3)
    MaterialAmount: int


class SiteBuilding(BaseModel):
    ReclaimableMaterials: List[SiteBuildingMaterial]
    RepairMaterials: List[SiteBuildingMaterial]

    SiteBuildingId: str = Field(min_length=65)
    BuildingId: str = Field(min_length=32)
    BuildingCreated: datetime
    BuildingName: str
    BuildingTicker: str = Field(max_length=3)
    BuildingLastRepair: Optional[datetime]
    Condition: float


class Site(BaseModel):
    Buildings: List[SiteBuilding]

    SiteId: str = Field(min_length=32)
    PlanetId: str = Field(min_length=32)
    PlanetIdentifier: str
    PlanetName: str
    PlanetFoundedEpochMs: datetime
    InvestedPermits: int
    MaximumPermits: int
    UserNameSubmitted: str
    Timestamp: NaiveDatetime


class SiteList(RootModel):
    root: List[Site]

    def __iter__(self):
        return iter(self.root)


class Warehouse(BaseModel):
    WarehouseId: str = Field(min_length=65)
    StoreId: str = Field(min_length=32)
    Units: int
    WeightCapacity: int
    VolumeCapacity: int
    NextPaymentTimestampEpochMs: datetime
    FeeAmount: int
    FeeCurrency: str
    FeeCollectorId: Optional[str]
    FeeCollectorName: Optional[str]
    FeeCollectorCode: Optional[str]
    LocationName: str
    LocationNaturalId: str
    UserNameSubmitted: str
    Timestamp: NaiveDatetime


class WarehouseList(RootModel):
    root: List[Warehouse]

    def __iter__(self):
        return iter(self.root)
