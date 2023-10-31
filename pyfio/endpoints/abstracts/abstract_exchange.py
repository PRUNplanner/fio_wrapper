class AbstractExchange:
    def get(self, exchange_ticker: str):
        raise NotImplementedError()

    def all(self):
        raise NotImplementedError()

    def get_full(self):
        raise NotImplementedError()

    def get_orders(self, company_code: str):
        raise NotImplementedError()

    def get_orders_exchange(self, company_code: str, exchange_code: str):
        raise NotImplementedError()
