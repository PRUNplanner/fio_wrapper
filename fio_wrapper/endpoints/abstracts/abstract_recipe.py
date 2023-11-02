class AbstractRecipe:
    def get(self, material_ticker: str):
        raise NotImplementedError()

    def all(self):
        raise NotImplementedError()
