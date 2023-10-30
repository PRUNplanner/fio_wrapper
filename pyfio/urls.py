class URLs:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

        # material
        self.material_base = "/material"
        self.material_allmaterials = "/allmaterials"

    # Material
    def material_url(self) -> str:
        return self.base_url + self.material_base

    def material_get_url(self, material_ticker: str) -> str:
        return self.material_url() + "/" + material_ticker

    def material_allmaterials_url(self) -> str:
        return self.material_url() + self.material_allmaterials

    def material_get_category(self, category_name: str) -> str:
        return self.material_url() + "/category/" + category_name
