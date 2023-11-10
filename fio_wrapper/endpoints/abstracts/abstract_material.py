from typing import Optional


class AbstractMaterial:
    def get(self, material_ticker: str, timeout: Optional[float] = None):
        raise NotImplementedError()

    def all(self, timeout: Optional[float] = None):
        raise NotImplementedError()

    def category(self, category_name: str, timeout: Optional[float] = None):
        raise NotImplementedError()
