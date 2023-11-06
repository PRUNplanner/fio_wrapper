# Generic


class EndpointNotImplemented(Exception):
    """Endpoint is not implemented in fio_wrapper"""

    pass


class NoAPIKeyProvided(Exception):
    """No FIO API Key was provided, but endpoint requires key"""

    pass


class NotAuthenticated(Exception):
    """FIO returned failed authentication"""

    pass


# Material


class MaterialTickerInvalid(Exception):
    """Invalid Material Ticker provided"""

    pass


class MaterialTickerNotFound(Exception):
    """Material Ticker not found"""

    pass


class MaterialCategoryNotFound(Exception):
    """Material Category not found"""

    pass


# Exchange


class ExchangeTickerInvalid(Exception):
    """Exchange ticker invalid"""

    pass


class ExchangeTickerNotFound(Exception):
    """Exchange ticker not found"""

    pass


class CompanyCodeInvalid(Exception):
    """Company code invalid"""

    pass


# Building


class BuildingTickerNotFound(Exception):
    """Building ticker not found"""

    pass


# Planet


class PlanetNotFound(Exception):
    """Planet not found"""

    pass


class PlanetSearchMaterialsInvalid(Exception):
    """Planet search material ticker provided invalid"""

    pass


class PlanetSearchDistanceChecksInvalid(Exception):
    """Planet search invalid distance checks"""

    pass


class PlanetSearchInvalidRequest(Exception):
    """Planet search request invalid"""

    pass


# LocalMarket


class InvalidAdType(Exception):
    """Ad type invalid"""

    pass


class PlanetOrAdsNotFound(Exception):
    """Planet or ads not found"""

    pass


class CompanyOrAdsNotFound(Exception):
    """Company or ads not found"""

    pass


# Sites


class NoSiteData(Exception):
    """No site data found"""

    pass


# Storage


class NoStorageData(Exception):
    """No storage data found"""

    pass
