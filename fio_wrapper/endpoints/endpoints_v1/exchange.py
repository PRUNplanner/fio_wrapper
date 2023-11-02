"""Access exchange information from FIO.
"""
from fio_wrapper.endpoints.abstracts.abstract_exchange import AbstractExchange
from fio_wrapper.fio_adapter import FIOAdapter
from fio_wrapper.validators import (
    validate_ticker,
    validate_exchange_code,
    validate_company_code,
)
from fio_wrapper.models.exchange_models import (
    ExchangeTickerFull,
    OrderList,
    ExchangeTickerList,
    ExchangeTickerFullList,
)
from fio_wrapper.exceptions import (
    ExchangeTickerInvalid,
    MaterialTickerInvalid,
    ExchangeTickerNotFound,
)


class Exchange(AbstractExchange):
    def __init__(self, adapter: FIOAdapter) -> None:
        self._adapter: FIOAdapter = adapter

    def _validate_exchangeticker(self, exchange_ticker: str) -> None:
        """Validates an exchange ticker

        Args:
            exchange_ticker (str): Exchange ticker

        Raises:
            ExchangeTickerInvalid: Exchange ticker can't be None type
            ExchangeTickerInvalid: Exchange ticker too short or long. Must be 5 to 7 characters
            ExchangeTickerInvalid: Exchange ticker must be of form MaterialTicker.ExchangeCode
            ExchangeTickerInvalid: Material ticker part of Exchange ticker invalid
        """
        if exchange_ticker is None:
            raise ExchangeTickerInvalid("Exchange ticker can't be None type")

        # min length: 5, max length: 7
        if len(exchange_ticker) < 5 or len(exchange_ticker) > 7:
            raise ExchangeTickerInvalid(
                "Exchange ticker to short or long. Must be 5 to 7 characters"
            )

        # must contain .
        if "." not in exchange_ticker:
            raise ExchangeTickerInvalid(
                "Exchange ticker must be of form MaterialTicker.ExchangeCode"
            )

        splitted = exchange_ticker.split(".")

        # validate Material part
        try:
            validate_ticker(material_ticker=splitted[0])
        except MaterialTickerInvalid as e:
            raise ExchangeTickerInvalid() from e

        # validate Exchange code
        validate_exchange_code(exchange_code=splitted[1])

    # /exchange/{ExchangeTicker}
    def get(self, exchange_ticker: str) -> ExchangeTickerFull:
        """Gets a single exchange ticker from FIO

        Args:
            exchange_ticker (str): Exchange Ticker (e.g., "DW.AI1")

        Raises:
            ExchangeTickerNotFound: Exchange ticker was not found

        Returns:
            ExchangeTicker: Exchange ticker
        """
        self._validate_exchangeticker(exchange_ticker=exchange_ticker)

        (status, data) = self._adapter.get(
            endpoint=self._adapter.urls.exchange_get_url(
                exchange_ticker=exchange_ticker
            ),
            err_codes=[204],
        )

        if status == 200:
            return ExchangeTickerFull.model_validate(data)
        elif status == 204:
            raise ExchangeTickerNotFound("Exchangeticker not found")

    # /exchange/all
    def all(self) -> ExchangeTickerList:
        """Gets all simple exchange ticker from FIO

        Returns:
            ExchangeTickerList: Exchange ticker
        """
        (_, data) = self._adapter.get(
            endpoint=self._adapter.urls.exchange_get_all_url()
        )

        return ExchangeTickerList.model_validate(data)

    # /exchange/full
    def full(self) -> ExchangeTickerFullList:
        """Gets a complete list of all exchange information from FIO

        Returns:
            ExchangeTickerFullList: Exchange ticker full
        """
        (_, data) = self._adapter.get(
            endpoint=self._adapter.urls.exchange_get_full_url()
        )

        return ExchangeTickerFullList.model_validate(data)

    # /exchange/orders/{CompanyCode}
    def get_orders(self, company_code: str) -> OrderList:
        """Gets a companies order data from FIO

        Args:
            company_code (str): Company code (1-4 characters)

        Returns:
            OrderList: Orders
        """
        # 1 to 4 character company code
        validate_company_code(company_code=company_code)

        (_, data) = self._adapter.get(
            endpoint=self._adapter.urls.exchange_get_orders_companycode(
                company_code=company_code
            ),
        )

        return OrderList.model_validate(data)

    # /exchange/orders/{CompanyCode}/{ExchangeCode}
    def get_orders_exchange(self, company_code: str, exchange_code: str) -> OrderList:
        """Gets a companies order data for a specific exchange from FIO

        Args:
            company_code (str): Company code (1-4 characters)
            exchange_code (str): Exchange code (e.g., "AI1")

        Returns:
            OrderList: Orders
        """
        validate_company_code(company_code=company_code)
        validate_exchange_code(exchange_code=exchange_code)

        (_, data) = self._adapter.get(
            self._adapter.urls.exchange_get_orders_companycode_exchange(
                company_code=company_code, exchange_code=exchange_code
            )
        )

        return OrderList.model_validate(data)
