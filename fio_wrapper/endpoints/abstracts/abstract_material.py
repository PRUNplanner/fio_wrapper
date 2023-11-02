class AbstractMaterial:
    def get(self, material_ticker: str):
        raise NotImplementedError()

    def all(self):
        raise NotImplementedError()

    def category(self, category_name: str):
        raise NotImplementedError()
