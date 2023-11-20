from fio_wrapper.config import Config


class URLs:
    """FIO API URLs

    Attributes:
        base_url (str): FIO Base URL
    """

    def __init__(self, config: Config) -> None:
        self.config = config

        self.base_url = config.base_url

        # material
        self.material_base = config.get_url("material_base")
        self.material_allmaterials = config.get_url("material_all")

        # exchange
        self.exchange_base = config.get_url("exchange_base")
        self.exchange_orders = config.get_url("exchange_orders")
        self.exchange_all = config.get_url("exchange_all")
        self.exchange_full = config.get_url("exchange_full")

        # building
        self.building_base = config.get_url("building_base")
        self.building_all = config.get_url("building_all")

        # recipe
        self.recipe_base = config.get_url("recipe_base")
        self.recipe_all = config.get_url("recipe_all")

        # planet
        self.planet_base = config.get_url("planet_base")
        self.planet_all = config.get_url("planet_all")
        self.planet_full = config.get_url("planet_full")
        self.planet_sites = config.get_url("planet_sites")
        self.planet_search = config.get_url("planet_search")

        # localmarket
        self.localmarket_base = config.get_url("localmarket_base")
        self.localmarket_planet = config.get_url("localmarket_planet")
        self.localmarket_shipping_source = config.get_url("localmarket_shipping_source")
        self.localmarket_shipping_destination = config.get_url(
            "localmarket_shipping_destination"
        )
        self.localmarket_company = config.get_url("localmarket_company")

        # sites
        self.sites_base = config.get_url("sites_base")
        self.sites_planets = config.get_url("sites_planets")
        self.sites_warehouses = config.get_url("sites_warehouses")

        # storage
        self.storage_base = config.get_url("storage_base")
        self.storage_planets = config.get_url("storage_planets")

        # groups
        self.groups = config.get_url("groups")
        self.groups_group = config.get_url("groups_group")
        self.groups_groupmemberships = config.get_url("groups_groupmemberships")
        self.groups_hub = config.get_url("groups_hub")
        self.groups_burn = config.get_url("groups_burn")

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
        return f"{self.base_url}{self.building_base}"

    def building_get_url(self, building_ticker: str) -> str:
        return f"{self.building_url()}/{building_ticker}"

    def building_get_all_url(self) -> str:
        return f"{self.building_url()}{self.building_all}"

    # Recipe
    def recipe_url(self) -> str:
        return f"{self.base_url}{self.recipe_base}"

    def recipe_get_url(self, material_ticker: str) -> str:
        return f"{self.recipe_url()}/{material_ticker}"

    def recipe_get_all_url(self) -> str:
        return f"{self.recipe_url()}{self.recipe_all}"

    # Planet

    def planet_url(self) -> str:
        return f"{self.base_url}{self.planet_base}"

    def planet_get_url(self, planet: str) -> str:
        return f"{self.planet_url()}/{planet}"

    def planet_all_url(self) -> str:
        return f"{self.planet_url()}{self.planet_all}"

    def planet_full_url(self) -> str:
        return f"{self.planet_url()}{self.planet_full}"

    def planet_sites_url(self, planet: str) -> str:
        return f"{self.planet_url()}{self.planet_sites}/{planet}"

    def planet_search_url(self) -> str:
        return f"{self.planet_url()}{self.planet_search}"

    # LocalMarket

    def localmarket_url(self) -> str:
        return f"{self.base_url}{self.localmarket_base}"

    def localmarket_planet_url(self, planet: str) -> str:
        return f"{self.localmarket_url()}{self.localmarket_planet}/{planet}"

    def localmarket_planet_type_url(self, planet: str, adtype: str) -> str:
        return f"{self.localmarket_url()}{self.localmarket_planet}/{planet}/{adtype}"

    def localmarket_shipping_source_url(self, planet: str) -> str:
        return f"{self.localmarket_url()}{self.localmarket_shipping_source}/{planet}"

    def localmarket_shipping_destination_url(self, planet: str) -> str:
        return (
            f"{self.localmarket_url()}{self.localmarket_shipping_destination}/{planet}"
        )

    def localmarket_company_url(self, companycode: str) -> str:
        return f"{self.localmarket_url()}{self.localmarket_company}/{companycode}"

    # Sites

    def sites_url(self) -> str:
        return f"{self.base_url}{self.sites_base}"

    def sites_get_url(self, username: str) -> str:
        return f"{self.sites_url()}/{username}"

    def sites_planets_get_url(self, username: str) -> str:
        return f"{self.sites_url()}{self.sites_planets}/{username}"

    def sites_planets_get_planet_url(self, username: str, planet: str) -> str:
        return f"{self.sites_url()}/{username}/{planet}"

    def sites_warehouses_get(self, username: str) -> str:
        return f"{self.sites_url()}{self.sites_warehouses}/{username}"

    # Storage
    def storage_url(self) -> str:
        return f"{self.base_url}{self.storage_base}"

    def storage_get_url(self, username: str) -> str:
        return f"{self.storage_url()}/{username}"

    def storage_planets_get_url(self, username: str) -> str:
        return f"{self.storage_url()}{self.storage_planets}/{username}"

    def storage_get_specific_url(self, username: str, specific: str) -> str:
        return f"{self.storage_url()}/{username}/{specific}"

    # Groups

    def group_all_url(self) -> str:
        return f"{self.base_url}{self.groups}"

    def group_get_url(self, groupid: int) -> str:
        return f"{self.base_url}{self.groups_group}/{groupid}"

    def group_memberships_url(self) -> str:
        return f"{self.base_url}{self.groups_groupmemberships}"

    def group_hub_url(self) -> str:
        return f"{self.base_url}{self.groups_hub}"

    def group_burn_url(self, groupid: int) -> str:
        return f"{self.base_url}{self.groups_burn}/{groupid}"
