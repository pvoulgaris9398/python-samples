class Price:
    def __init__(
        self, symbol, open, high, low, close, volume, price_dt, exchange="NYSE"
    ):
        self.symbol = symbol
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.price_dt = price_dt
        self.exchange = exchange

    def __str__(self):
        return f"{self.symbol}: Open: {self.open} Close: {self.close} Date: {self.price_dt}"  # noqa
