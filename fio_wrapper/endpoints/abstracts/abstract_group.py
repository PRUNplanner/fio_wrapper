from typing import List, Optional


class AbstractGroup:
    def all(self, timeout: Optional[float] = None):
        raise NotImplementedError()

    def get(self, groupid: int, timeout: Optional[float] = None):
        raise NotImplementedError()

    def memberships(self, timeout: Optional[float] = None):
        raise NotImplementedError()

    def hub(self, members: List[str], timeout: Optional[float] = None):
        raise NotImplementedError()

    def burn(self, groupid: int, timeout: Optional[float] = None):
        raise NotImplementedError()
