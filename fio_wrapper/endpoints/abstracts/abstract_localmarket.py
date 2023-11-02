class AbstractLocalMarket:
    # /localmarket/planet/{Planet}
    def planet(self, planet: str):
        raise NotImplementedError()

    # /localmarket/planet/{Planet}/{Type}
    def planet_buy(self, planet: str):
        raise NotImplementedError()

    def planet_sell(self, planet: str):
        raise NotImplementedError()

    def planet_shipping(self, planet: str):
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
