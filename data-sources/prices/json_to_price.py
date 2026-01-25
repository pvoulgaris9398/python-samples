import json  # noqa

"""
todo: finish parsing
"""


def parse(json_data):
    symbol = json_data["Meta Data"]["2. Symbol"]

    prices = json_data["Time Series (Daily)"]

    print(prices)

    return symbol
