from typing import Optional


class AbstractStorage:
    def get(self, username: str, timeout: Optional[float] = None):
        raise NotImplementedError()

    def get_specific(
        self, username: str, specific: str, timeout: Optional[float] = None
    ):
        raise NotImplementedError()

    def planets(self, username: str, timeout: Optional[float] = None):
        raise NotImplementedError()
