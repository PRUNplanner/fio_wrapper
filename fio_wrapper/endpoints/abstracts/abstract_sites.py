class AbstractSites:
    def get(self, username: str):
        raise NotImplemented()

    def planets(self, username: str):
        raise NotImplemented()
