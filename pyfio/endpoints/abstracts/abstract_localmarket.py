class AbstractLocalMarket:
    # /localmarket/{LocalMarketId}
    def get(self, localmarket_id: str):
        raise NotImplementedError()

    # /localmarket/planet/{Planet}
    def planet(self, planet: str):
        raise NotImplementedError()

    # /localmarket/planet/{Planet}/{Type}
    def planet_type(self, planet: str, type: str):
        raise NotImplementedError()

    # /localmarket/shipping/source/{SourcePlanet}
    def shipping_from(self, planet: str):
        raise NotImplementedError()

    # /localmarket/shipping/destination/{DestinationPlanet}
    def shipping_to(self, planet: str):
        raise NotImplementedError()

    # /localmarket/company/{Company}
    def company(self, companycode: str):
        raise NotImplementedError()
