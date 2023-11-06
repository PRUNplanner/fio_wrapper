class AbstractStorage:
    def get(self, username: str):
        raise NotImplemented()

    def get_specific(self, username: str, specific: str):
        raise NotImplemented()

    def planets(self, username: str):
        raise NotImplemented()
