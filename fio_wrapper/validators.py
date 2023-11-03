from typing import List
from fio_wrapper.exceptions import (
    InvalidAdType,
    MaterialTickerInvalid,
    ExchangeTickerInvalid,
    CompanyCodeInvalid,
)


def validate_ticker(material_ticker: str) -> None:
    """Validates a material ticker

    Args:
        material_ticker (str): Material ticker

    Raises:
        MaterialTickerInvalid: Material ticker can't be None type
        MaterialTickerInvalid: Material ticker can't be longer than 3 characters
        MaterialTickerInvalid: Material ticker can't be shorter than 1 character
        MaterialTickerInvalid: Material ticker can't contain spaces
    """
    if material_ticker is None:
        raise MaterialTickerInvalid("Material ticker can't be None type")
    if len(material_ticker) > 3:
        raise MaterialTickerInvalid("Material ticker can't be longer than 3 characters")

    if len(material_ticker) < 1:
        raise MaterialTickerInvalid(
            "Material ticker can't be shorter than 1 characters"
        )

    if " " in material_ticker:
        raise MaterialTickerInvalid("Material ticker can't contain spaces")


def validate_exchange_code(exchange_code: str) -> None:
    if exchange_code is None:
        raise ExchangeTickerInvalid("Exchange code can't be None type")

    if len(exchange_code) != 3:
        raise ExchangeTickerInvalid("Exchange code too short. Must have 3 characters")

    # first 2 characters must be str
    if (
        type(exchange_code[0]) != str
        or type(exchange_code[1]) != str
        or not exchange_code[2].isnumeric()
    ):
        raise ExchangeTickerInvalid(
            "Exchange code must begin with exchange ticker (e.g., AI)"
        )

    # last character must be int


def validate_company_code(company_code: str) -> None:
    if company_code == "" or company_code is None:
        raise CompanyCodeInvalid("Invalid company code. Can't be empty or None type")

    if len(company_code) > 4:
        raise CompanyCodeInvalid("Invalid company code. Must be 1 to 4 characters")


def validate_localmarket_adtype(adtype: str) -> None:
    accepted_types: List[str] = [
        "BUY",
        "BUYS",
        "BUYING",
        "SELL",
        "SELLS",
        "SELLING",
        "SHIP",
        "SHIPPING",
    ]

    if not adtype in accepted_types:
        raise InvalidAdType("Invalid ad type")


def validate_planet_search_materials(materials: List[str]) -> bool:
    if materials is None:
        return False

    if len(materials) > 4:
        return False

    for material in materials:
        if len(material) == 0 or len(material) > 3:
            return False

    return True


def validate_planet_search_distance_checks(distance_checks: List[str]) -> bool:
    if distance_checks is None:
        return False

    if len(distance_checks) > 3:
        return False

    return True
