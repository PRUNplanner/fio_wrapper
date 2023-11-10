from typing import List


class AbstractGroup:
    def all(self, timeout: float | None = None):
        raise NotImplementedError()

    def get(self, groupid: int, timeout: float | None = None):
        raise NotImplementedError()

    def memberships(self, timeout: float | None = None):
        raise NotImplementedError()

    def hub(self, members: List[str], timeout: float | None = None):
        raise NotImplementedError()

    def burn(self, groupid: int, timeout: float | None = None):
        raise NotImplementedError()
