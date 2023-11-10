from typing import Optional


class AbstractExchange:
    def get(self, exchange_ticker: str, timeout: Optional[float] = None):
        raise NotImplementedError()

    def all(self, timeout: Optional[float] = None):
        raise NotImplementedError()

    def get_full(self, timeout: Optional[float] = None):
        raise NotImplementedError()

    def get_orders(self, company_code: str, timeout: Optional[float] = None):
        raise NotImplementedError()

    def get_orders_exchange(
        self, company_code: str, exchange_code: str, timeout: Optional[float] = None
    ):
        raise NotImplementedError()
