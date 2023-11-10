from typing import List, Optional
from datetime import datetime, timedelta
from pydantic import BaseModel, RootModel, Field, AwareDatetime, NaiveDatetime


class GroupAdmin(BaseModel):
    GroupAdminUserName: str


class GroupUser(BaseModel):
    GroupUserName: str


class Group(BaseModel):
    GroupAdmins: List[GroupAdmin]
    GroupUsers: List[GroupUser]
    GroupModelId: int
    GroupOwner: str
    GroupName: str

    def users(self) -> List[str]:
        return [user.GroupUserName.upper() for user in self.GroupUsers]


class GroupList(RootModel):
    root: List[Group]

    def __iter__(self):
        """Iterates through all Groups

        Returns:
            Group: Group element
        """
        return iter(self.root)

    def ids(self) -> List[int]:
        """Returns a list of Group IDs from all Groups in the List

        Returns:
            List[int]: List of GroupModelId
        """
        return [group.GroupModelId for group in self.root]


class GroupMembership(BaseModel):
    GroupName: str
    GroupId: int


class GroupMembershipList(RootModel):
    root: List[GroupMembership]

    def __iter__(self):
        """Iterates through all group memberships

        Returns:
            GroupMembership: Group membership element
        """
        return iter(self.root)

    def ids(self) -> List[int]:
        """Returns a list of Group IDs from all Group Memberships

        Returns:
            List[int]: List of GroupIDs
        """
        return [membership.GroupId for membership in self.root]


class StorageItem(BaseModel):
    MaterialTicker: Optional[str] = Field(max_length=3)
    MaterialName: Optional[str]
    MaterialCategoryName: Optional[str]
    Units: int


class PlayerCXWarehouses(BaseModel):
    PlayerName: str
    StorageType: str
    Items: List[StorageItem]


class CXWarehouse(BaseModel):
    WarehouseLocationName: str
    WarehouseLocationNaturalId: str
    PlayerCXWarehouses: List[PlayerCXWarehouses]


class RepairMaterial(BaseModel):
    MaterialTicker: str = Field(max_length=3)
    Amount: int


class AddressLine(BaseModel):
    LineId: str = Field(min_length=32)
    LineType: str
    NaturalId: str
    Name: str


class AddressLineFlight(BaseModel):
    LineId: str = Field(min_length=32)
    Type: str
    LineNaturalId: str
    LineName: str


class ShipFuel(BaseModel):
    CurrentSF: int
    MaxSF: int
    CurrentFF: int
    MaxFF: int


class ShipCargo(BaseModel):
    PlayerName: str
    StorageType: str
    Items: List[StorageItem]
    LastUpdated: NaiveDatetime


class ShipFlightSegment(BaseModel):
    OriginLines: List[AddressLineFlight]
    DestinationLines: List[AddressLineFlight]

    Type: str
    DepartureTimeEpochMs: datetime
    ArrivalTimeEpochMs: datetime
    StlDistance: Optional[float]
    StlFuelConsumption: Optional[float]
    FtlDistance: Optional[float]
    FtlFuelConsumption: Optional[float]
    Origin: str
    Destination: str


class ShipFlight(BaseModel):
    Segments: List[ShipFlightSegment]

    FlightId: str = Field(min_length=32)
    ShipId: str = Field(min_length=32)
    Origin: str
    Destination: str
    DepartureTimeEpochMs: datetime
    ArrivalTimeEpochMs: datetime
    CurrentSegmentIndex: int
    StlDistance: float
    FtlDistance: float
    IsAborted: bool
    Timestamp: NaiveDatetime


class PlayerShip(BaseModel):
    PlayerName: str
    ShipName: Optional[str]
    ShipRegistration: str
    Location: str
    Destination: Optional[str]
    LocationETA: Optional[AwareDatetime]
    LocationETALocalTime: Optional[AwareDatetime]
    Condition: float

    RepairMaterials: List[RepairMaterial]
    AddressLines: List[AddressLine]

    Flight: Optional[ShipFlight]
    Fuel: ShipFuel
    Cargo: ShipCargo

    LastUpdated: NaiveDatetime


class Currency(BaseModel):
    CurrencyName: str
    Amount: float
    LastUpdated: NaiveDatetime


class Material(BaseModel):
    MaterialTicker: str = Field(max_length=3)
    MaterialName: str
    MaterialCategoryName: Optional[str]
    Units: int


class ProductionLine(BaseModel):
    Started: bool
    Halted: bool
    Recurring: bool
    OrderDuration: timedelta
    TimeCompletion: NaiveDatetime
    Inputs: List[Material]
    Outputs: List[Material]
    LastUpdated: NaiveDatetime
    BuildingName: str
    BuildingTicker: str = Field(max_length=3)
    Capacity: int
    Efficiency: float
    Condition: float


class Building(BaseModel):
    BuildingName: str
    BuildingTicker: str = Field(max_length=3)
    Condition: float
    RepairMaterials: List[Material]
    ReclaimableMaterials: List[Material]
    ProductionLiness: List[ProductionLine]


class Storage(BaseModel):
    PlayerName: str
    StorageType: str
    Items: List[Material]
    LastUpdated: NaiveDatetime


class Location(BaseModel):
    LocationIdentifier: str
    LocationName: str
    Buildings: List[Building]
    BaseStorage: Storage
    WarehouseStorage: Storage
    StationaryPlayerShips: List[PlayerShip]


class PlayerModel(BaseModel):
    Username: str
    Currencies: List[Currency]
    Locations: List[Location]


class GroupHub(BaseModel):
    GroupName: Optional[str]
    CXWarehouses: List[CXWarehouse]
    PlayerShipsInFlight: List[PlayerShip]
    PlayerStationaryShips: List[PlayerShip]
    Failures: List[str]


class Inventory(BaseModel):
    MaterialId: str = Field(min_length=32)
    MaterialTicker: Optional[str] = Field(max_length=3)
    MaterialAmount: int


class Consumption(BaseModel):
    MaterialId: str = Field(min_length=32)
    MaterialTicker: str = Field(max_length=3)
    DailyAmount: float


class Burn(BaseModel):
    RequesterUserName: str
    UserName: str
    Error: Optional[str]
    PlanetId: Optional[str] = Field(min_length=32)
    PlanetName: Optional[str]
    PlanetNaturalId: Optional[str]
    PlanetConsumptionTime: Optional[NaiveDatetime]
    LastUpdate: NaiveDatetime
    LastUpdateCause: Optional[str]

    Inventory: List[Inventory]
    WorkforceConsumption: List[Consumption]
    OrderConsumption: List[Consumption]
    OrderProduction: List[Consumption]


class BurnList(RootModel):
    root: List[Burn]

    def __iter__(self):
        """Iterates through all burn elements

        Returns:
            Burn: Burn element
        """
        return iter(self.root)
