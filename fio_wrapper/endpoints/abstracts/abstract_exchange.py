class AbstractExchange:
    def get(self, exchange_ticker: str, timeout: float | None = None):
        raise NotImplementedError()

    def all(self, timeout: float | None = None):
        raise NotImplementedError()

    def get_full(self, timeout: float | None = None):
        raise NotImplementedError()

    def get_orders(self, company_code: str, timeout: float | None = None):
        raise NotImplementedError()

    def get_orders_exchange(
        self, company_code: str, exchange_code: str, timeout: float | None = None
    ):
        raise NotImplementedError()
