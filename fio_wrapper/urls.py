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

        # building
        self.building_base = "/building"
        self.building_all = "/allbuildings"

        # recipe
        self.recipe_base = "/recipes"
        self.recipe_all = "/allrecipes"

        # planet
        self.planet_base = "/planet"
        self.planet_all = "/allplanets"
        self.planet_full = "/allplanets/full"
        self.planet_sites = "/sites"
        self.planet_search = "/search"

        # localmarket
        self.localmarket_base = "/localmarket"
        self.localmarket_planet = "/planet"
        self.localmarket_shipping_source = "/shipping/source"
        self.localmarket_shipping_destination = "/shipping/destination"
        self.localmarket_company = "/company"

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

    # Building
    def building_url(self) -> str:
        return self.base_url + self.building_base

    def building_get_url(self, building_ticker: str) -> str:
        return self.building_url() + "/" + building_ticker

    def building_get_all_url(self) -> str:
        return self.building_url() + self.building_all

    # Recipe
    def recipe_url(self) -> str:
        return self.base_url + self.recipe_base

    def recipe_get_url(self, material_ticker: str) -> str:
        return self.recipe_url() + "/" + material_ticker

    def recipe_get_all_url(self) -> str:
        return self.recipe_url() + self.recipe_all

    # Planet

    def planet_url(self) -> str:
        return self.base_url + self.planet_base

    def planet_get_url(self, planet: str) -> str:
        return self.planet_url() + "/" + planet

    def planet_all_url(self) -> str:
        return self.planet_url() + self.planet_all

    def planet_full_url(self) -> str:
        return self.planet_url() + self.planet_full

    def planet_sites_url(self, planet: str) -> str:
        return self.planet_url() + self.planet_sites + "/" + planet

    def planet_search_url(self) -> str:
        return self.planet_url() + self.planet_search

    # LocalMarket

    def localmarket_url(self) -> str:
        return self.base_url + self.localmarket_base

    def localmarket_planet_url(self, planet: str) -> str:
        return self.localmarket_url() + self.localmarket_planet + "/" + planet

    def localmarket_planet_type_url(self, planet: str, adtype: str) -> str:
        return (
            self.localmarket_url()
            + self.localmarket_planet
            + "/"
            + planet
            + "/"
            + adtype
        )

    def localmarket_shipping_source_url(self, planet: str) -> str:
        return self.localmarket_url() + self.localmarket_shipping_source + "/" + planet

    def localmarket_shipping_destination_url(self, planet: str) -> str:
        return (
            self.localmarket_url()
            + self.localmarket_shipping_destination
            + "/"
            + planet
        )

    def localmarket_company_url(self, companycode: str) -> str:
        return self.localmarket_url() + self.localmarket_company + "/" + companycode
