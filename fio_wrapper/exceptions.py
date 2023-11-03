# Not Implemented


class EndpointNotImplemented(Exception):
    pass


# Material


class MaterialTickerInvalid(Exception):
    pass


class MaterialTickerNotFound(Exception):
    pass


class MaterialCategoryNotFound(Exception):
    pass


# Exchange


class ExchangeTickerInvalid(Exception):
    pass


class ExchangeTickerNotFound(Exception):
    pass


class CompanyCodeInvalid(Exception):
    pass


# Building


class BuildingTickerNotFound(Exception):
    pass


# Planet


class PlanetNotFound(Exception):
    pass


class PlanetSearchMaterialsInvalid(Exception):
    pass


class PlanetSearchDistanceChecksInvalid(Exception):
    pass


class PlanetSearchInvalidRequest(Exception):
    pass


# LocalMarket


class InvalidAdType(Exception):
    pass


class PlanetOrAdsNotFound(Exception):
    pass


class CompanyOrAdsNotFound(Exception):
    pass
