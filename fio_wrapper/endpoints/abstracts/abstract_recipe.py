class AbstractRecipe:
    def get(self, material_ticker: str, timeout: float | None = None):
        raise NotImplementedError()

    def all(self, timeout: float | None = None):
        raise NotImplementedError()
