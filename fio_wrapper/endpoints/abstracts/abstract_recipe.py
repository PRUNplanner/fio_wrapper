from typing import Optional


class AbstractRecipe:
    def get(self, material_ticker: str, timeout: Optional[float] = None):
        raise NotImplementedError()

    def all(self, timeout: Optional[float] = None):
        raise NotImplementedError()
