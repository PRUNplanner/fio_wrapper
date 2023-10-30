class URLs:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

        # material
        self.material_base = "/material"
        self.material_allmaterials = "/allmaterials"

        # exchange
        self.exchange_base = "/exchange"
        self.exchange_orders = "/orders"
        self.exchange_all = "/all"
        self.exchange_full = "/full"

    # Material
    def material_url(self) -> str:
        return self.base_url + self.material_base

    def material_get_url(self, material_ticker: str) -> str:
        return self.material_url() + "/" + material_ticker

    def material_allmaterials_url(self) -> str:
        return self.material_url() + self.material_allmaterials

    def material_get_category(self, category_name: str) -> str:
        return self.material_url() + "/category/" + category_name

    # Exchange
    def exchange_url(self) -> str:
        return self.base_url + self.exchange_base

    def exchange_get_url(self, exchange_ticker: str) -> str:
        return self.exchange_url() + "/" + exchange_ticker

    def exchange_get_all_url(self) -> str:
        return self.exchange_url() + self.exchange_all

    def exchange_get_full_url(self) -> str:
        return self.exchange_url() + self.exchange_full

    def exchange_get_orders_companycode(self, company_code: str) -> str:
        return self.exchange_url() + self.exchange_orders + "/" + company_code

    def exchange_get_orders_companycode_exchange(
        self, company_code: str, exchange_code: str
    ) -> str:
        return (
            self.exchange_url()
            + self.exchange_orders
            + "/"
            + company_code
            + "/"
            + exchange_code
        )
