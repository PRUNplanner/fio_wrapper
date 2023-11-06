from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, RootModel, Field, NaiveDatetime


class StorageItem(BaseModel):
    MaterialId: str = Field(min_length=32)
    MaterialName: Optional[str]
    MaterialTicker: Optional[str] = Field(max_length=3, default=None)
    MaterialCategory: Optional[str] = Field(min_length=32, default=None)
    MaterialWeight: float
    MaterialVolume: float
    MaterialAmount: int
    MaterialValue: float
    MaterialValueCurrency: Optional[str]
    Type: str
    TotalWeight: float
    TotalVolume: float


class Storage(BaseModel):
    StorageItems: Optional[List[StorageItem]]
    StorageId: str = Field(min_length=32)
    AddressableId: str = Field(min_length=32)
    Name: Optional[str]
    Type: str
    UserNameSubmitted: str
    Timestamp: datetime
    WeightCapacity: int
    VolumeCapacity: int
    UserNameSubmitted: str
    Timestamp: NaiveDatetime


class StorageList(RootModel):
    root: List[Storage]

    def __iter__(self):
        return iter(self.root)
