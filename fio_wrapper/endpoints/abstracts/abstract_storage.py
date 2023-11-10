class AbstractStorage:
    def get(self, username: str):
        raise NotImplementedError()

    def get_specific(self, username: str, specific: str):
        raise NotImplementedError()

    def planets(self, username: str):
        raise NotImplementedError()
