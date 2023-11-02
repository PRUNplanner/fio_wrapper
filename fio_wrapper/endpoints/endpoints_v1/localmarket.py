"""Access local market information from FIO.
"""
from typing import Tuple
from fio_wrapper.endpoints.abstracts.abstract_localmarket import AbstractLocalMarket
from fio_wrapper.exceptions import (
    CompanyOrAdsNotFound,
    PlanetNotFound,
    PlanetOrAdsNotFound,
)
from fio_wrapper.fio_adapter import FIOAdapter
from fio_wrapper.models.localmarket_models import (
    LocalMarketAdList,
    LocalMarketAds,
    LocalMarketShippingAdList,
)
from fio_wrapper.validators import validate_localmarket_adtype


class LocalMarket(AbstractLocalMarket):
    def __init__(self, adapter: FIOAdapter) -> None:
        self._adapter: FIOAdapter = adapter

    # /localmarket/planet/{Planet}
    def planet(self, planet: str) -> LocalMarketAds:
        """Gets local market ads for planet

        Args:
            planet (str): PlanetId, PlanetNaturalId, PlanetName

        Raises:
            PlanetNotFound: Planet not found

        Returns:
            LocalMarketAds: List of ads
        """
        (status, data) = self._adapter.get(
            endpoint=self._adapter.urls.localmarket_planet_url(planet), err_codes=[204]
        )

        if status == 200:
            return LocalMarketAds.model_validate(data)
        elif status == 204:
            raise PlanetNotFound("Planet not found")

    def _planet_type(self, planet: str, adtype: str) -> Tuple[int, any]:
        validate_localmarket_adtype(adtype=adtype)

        return self._adapter.get(
            endpoint=self._adapter.urls.localmarket_planet_type_url(
                planet=planet, adtype=adtype
            ),
            err_codes=[204],
        )

    # /localmarket/planet/{Planet}/{Type}
    def planet_buy(self, planet: str) -> LocalMarketAdList:
        """Gets all BUY ads from the planets local market

        Args:
            planet (str): PlanetId, PlanetNaturalId, PlanetName

        Raises:
            PlanetOrAdsNotFound: Planet not found or no ads

        Returns:
            LocalMarketAdList: List of planet local market BUY ads
        """
        (status, data) = self._planet_type(planet=planet, adtype="BUY")

        if status == 200:
            return LocalMarketAdList.model_validate(data)
        elif status == 204:
            raise PlanetOrAdsNotFound("Planet not found or no ads on planet")

    def planet_sell(self, planet: str) -> LocalMarketAdList:
        """Gets all SELL ads from planets local market

        Args:
            planet (str): PlanetId, PlanetNaturalId, PlanetName

        Raises:
            PlanetOrAdsNotFound: Planet not found or no ads

        Returns:
            LocalMarketAdList: List of planet local market SELL ads
        """
        (status, data) = self._planet_type(planet=planet, adtype="SELL")

        if status == 200:
            return LocalMarketAdList.model_validate(data)
        elif status == 204:
            raise PlanetOrAdsNotFound("Planet not found or no ads on planet")

    def planet_shipping(self, planet: str) -> LocalMarketShippingAdList:
        """Gets a list of planets shipping ads

        Args:
            planet (str): PlanetId, PlanetNaturalId, PlanetName

        Raises:
            PlanetOrAdsNotFound: Planet not found or no ads

        Returns:
            LocalMarketShippingAdList: List of planet local market SHIPPING ads
        """
        (status, data) = self._planet_type(planet=planet, adtype="SHIP")

        if status == 200:
            return LocalMarketShippingAdList.model_validate(data)
        elif status == 204:
            raise PlanetOrAdsNotFound("Planet not found or no ads on planet")

    # /localmarket/shipping/source/{SourcePlanet}
    def shipping_from(self, planet: str) -> LocalMarketShippingAdList:
        """Gets a list of SHIPPING ads starting from planet

        Args:
            planet (str): PlanetId, PlanetNaturalId, PlanetName

        Raises:
            PlanetOrAdsNotFound: Planet not found or no ads

        Returns:
            LocalMarketShippingAdList: List of shipping ads from planet
        """
        (status, data) = self._adapter.get(
            endpoint=self._adapter.urls.localmarket_shipping_source_url(planet=planet),
            err_codes=[204],
        )

        if status == 200:
            return LocalMarketShippingAdList.model_validate(data)
        elif status == 204:
            raise PlanetOrAdsNotFound("Planet not found or no ads on planet")

    # /localmarket/shipping/destination/{DestinationPlanet}
    def shipping_to(self, planet: str) -> LocalMarketShippingAdList:
        """Gets a list of SHIPPING ads ending at planet

        Args:
            planet (str): PlanetId, PlanetNaturalId, PlanetName

        Raises:
            PlanetOrAdsNotFound: Planet not found or no ads

        Returns:
            LocalMarketShippingAdList: List of shipping ads to planet
        """
        (status, data) = self._adapter.get(
            endpoint=self._adapter.urls.localmarket_shipping_destination_url(
                planet=planet
            ),
            err_codes=[204],
        )

        if status == 200:
            return LocalMarketShippingAdList.model_validate(data)
        elif status == 204:
            raise PlanetOrAdsNotFound("Planet not found or no ads on planet")

    # /localmarket/company/{Company}
    def company(self, companycode: str) -> LocalMarketAds:
        """Gets a list of all ads of the specified company

        Args:
            companycode (str): Company Code (e.g., "SKYP")

        Raises:
            CompanyOrAdsNotFound: Company not found or company has no ads

        Returns:
            LocalMarketAds: List of local market ads of company
        """
        (status, data) = self._adapter.get(
            endpoint=self._adapter.urls.localmarket_company_url(
                companycode=companycode
            ),
            err_codes=[204],
        )

        if status == 200:
            return LocalMarketAds.model_validate(data)
        elif status == 204:
            raise CompanyOrAdsNotFound("Company not found or no ads from company")
