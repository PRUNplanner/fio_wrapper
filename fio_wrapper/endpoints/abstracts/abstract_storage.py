class AbstractStorage:
    def get(self, username: str, timeout: float | None = None):
        raise NotImplementedError()

    def get_specific(self, username: str, specific: str, timeout: float | None = None):
        raise NotImplementedError()

    def planets(self, username: str, timeout: float | None = None):
        raise NotImplementedError()
