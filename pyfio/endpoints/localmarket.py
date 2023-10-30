from pyfio.fio_adapter import FIOAdapter


class LocalMarket:
    def __init__(self, adapter: FIOAdapter) -> None:
        self._adapter: FIOAdapter = adapter

    # /localmarket/{LocalMarketId}

    # /localmarket/planet/{Planet}

    # /localmarket/planet/{Planet}/{Type}

    # /localmarket/shipping/source/{SourcePlanet}

    # /localmarket/shipping/destination/{DestinationPlanet}

    # /localmarket/company/{Company}
