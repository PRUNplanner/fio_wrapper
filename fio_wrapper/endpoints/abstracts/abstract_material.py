class AbstractMaterial:
    def get(self, material_ticker: str, timeout: float | None = None):
        raise NotImplementedError()

    def all(self, timeout: float | None = None):
        raise NotImplementedError()

    def category(self, category_name: str, timeout: float | None = None):
        raise NotImplementedError()
