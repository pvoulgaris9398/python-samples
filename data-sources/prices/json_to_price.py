import json  # noqa
import price as prc

"""
todo: finish parsing
"""


def parse2(json_data):
    symbol = json_data["Meta Data"]["2. Symbol"]

    prices = json_data["Time Series (Daily)"]

    for price_dt in iter(prices):
        price_record = prices[price_dt]
        yield prc.Price(
            symbol,
            price_record["1. open"],
            price_record["2. high"],
            price_record["3. low"],
            price_record["4. close"],
            price_record["5. volume"],
            price_dt,
        )


def parse(json_data):
    symbol = json_data["Meta Data"]["2. Symbol"]

    prices = json_data["Time Series (Daily)"]
    # print(prices)

    # print("\n")
    for price_dt in iter(prices):
        # print(price_dt)
        for price_type in prices[price_dt]:
            price = prices[price_dt][price_type]
            # print(f"{price_type}: {price}")
            yield (symbol, price_dt, price_type, price)

    # price1 = prices[0]
    # print(price1)

    # return symbol
