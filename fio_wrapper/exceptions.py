# Generic


class EndpointNotImplemented(Exception):
    """Endpoint is not implemented in fio_wrapper"""


class NoAPIKeyProvided(Exception):
    """No FIO API Key was provided, but endpoint requires key"""


class NotAuthenticated(Exception):
    """FIO returned failed authentication"""


class UnknownFIOResponse(Exception):
    """FIO returned a unknown response"""


# Material


class MaterialTickerInvalid(Exception):
    """Invalid Material Ticker provided"""


class MaterialTickerNotFound(Exception):
    """Material Ticker not found"""


class MaterialCategoryNotFound(Exception):
    """Material Category not found"""


# Exchange


class ExchangeTickerInvalid(Exception):
    """Exchange ticker invalid"""


class ExchangeTickerNotFound(Exception):
    """Exchange ticker not found"""


class CompanyCodeInvalid(Exception):
    """Company code invalid"""


# Building


class BuildingTickerNotFound(Exception):
    """Building ticker not found"""


# Planet


class PlanetNotFound(Exception):
    """Planet not found"""


class PlanetSearchMaterialsInvalid(Exception):
    """Planet search material ticker provided invalid"""


class PlanetSearchDistanceChecksInvalid(Exception):
    """Planet search invalid distance checks"""


class PlanetSearchInvalidRequest(Exception):
    """Planet search request invalid"""


# LocalMarket


class InvalidAdType(Exception):
    """Ad type invalid"""


class PlanetOrAdsNotFound(Exception):
    """Planet or ads not found"""


class CompanyOrAdsNotFound(Exception):
    """Company or ads not found"""


# Sites


class NoSiteData(Exception):
    """No site data found"""


# Storage


class NoStorageData(Exception):
    """No storage data found"""
