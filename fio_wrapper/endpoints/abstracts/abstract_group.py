from typing import List


class AbstractGroup:
    def all(self):
        raise NotImplementedError()

    def get(self, groupid: int):
        raise NotImplementedError()

    def memberships(self):
        raise NotImplementedError()

    def hub(self, members: List[str]):
        raise NotImplementedError()

    def burn(self, groupid: int):
        raise NotImplementedError()
