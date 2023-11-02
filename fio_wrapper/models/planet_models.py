from typing import List, Optional
from pydantic import BaseModel, RootModel, Field, NaiveDatetime
from datetime import datetime


class PlanetResource(BaseModel):
    MaterialId: str = Field(min_length=32)
    ResourceType: str
    Factor: float


class BuildingRequirement(BaseModel):
    MaterialName: str
    MaterialId: str = Field(min_length=32)
    MaterialTicker: str = Field(max_length=3)
    MaterialCategory: str = Field(min_length=32)
    MaterialAmount: int
    MaterialWeight: float
    MaterialVolume: float


class ProductionFee(BaseModel):
    Category: str
    WorkforceLevel: str
    FeeAmount: int
    FeeCurrency: Optional[str]


class COGCProgram(BaseModel):
    ProgramType: Optional[str]
    StartEpochMs: datetime
    EndEpochMs: datetime


class COGCVote(BaseModel):
    CompanyName: str
    CompanyCode: str
    Influence: float
    VoteType: str
    VoteTimeEpochMs: datetime


class Planet(BaseModel):
    PlanetNaturalId: str
    PlanetName: str


class PlanetList(RootModel):
    root: List[Planet]

    def __iter__(self):
        return iter(self.root)


class PlanetFull(Planet):
    Resources: List[PlanetResource]
    BuildRequirements: List[BuildingRequirement]
    ProductionFees: List[ProductionFee]
    COGCPrograms: List[COGCProgram]
    COGCVotes: List[COGCVote]

    PlanetId: str = Field(min_length=32)
    Namer: Optional[str]
    NamingDataEpochMs: int
    Nameable: bool
    SystemId: str = Field(min_length=32)
    Gravity: float
    MagneticField: float
    Mass: float
    MassEarth: float
    OrbitSemiMajorAxis: int
    OrbitEccentricity: float
    OrbitInclination: float
    OrbitRightAscension: int
    OrbitPeriapsis: int
    OrbitIndex: int
    Pressure: float
    Radiation: float
    Radius: float
    Sunlight: float
    Surface: bool
    Temperature: float
    Fertility: float
    HasLocalMarket: bool
    HasChamberOfCommerce: bool
    HasWarehouse: bool
    HasAdministrationCenter: bool
    HasShipyard: bool
    FactionCode: Optional[str]
    FactionName: Optional[str]
    GovernorId: Optional[str] = Field(min_length=32)
    GovernorUserName: Optional[str]
    GovernorCorporationId: Optional[str] = Field(min_length=32)
    GovernorCorporationName: Optional[str]
    GovernorCorporationCode: Optional[str]
    CurrencyName: Optional[str]
    CurrencyCode: Optional[str]
    CollectorId: Optional[str] = Field(min_length=32)
    CollectorName: Optional[str]
    CollectorCode: Optional[str]
    BaseLocalMarketFee: int
    LocalMarketFeeFactor: int
    WarehouseFee: int
    PopulationId: Optional[str] = Field(min_length=32)
    COGCProgramStatus: Optional[str]
    PlanetTier: int
    UserNameSubmitted: str
    Timestamp: NaiveDatetime


class PlanetFullList(RootModel):
    root: List[PlanetFull]

    def __iter__(self):
        return iter(self.root)


class PlanetSite(BaseModel):
    PlanetId: str = Field(min_length=32)
    OwnerId: str = Field(min_length=32)
    OwnerName: str
    OwnerCode: Optional[str]
    PlotNumber: int
    PlotId: str = Field(min_length=32)
    SiteId: str


class PlanetSiteList(RootModel):
    root: List[PlanetSite]

    def __iter__(self):
        return iter(self.root)
