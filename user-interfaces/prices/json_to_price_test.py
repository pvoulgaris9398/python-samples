#!/usr/bin/env python3

import itertools
import json
from operator import itemgetter

import json_to_price as jtp
import pandas as pd
import price as prc

json_data = """{
    "Meta Data": {
        "1. Information": "Daily Prices (open, high, low, close) and Volumes",
        "2. Symbol": "IBM",
        "3. Last Refreshed": "2026-01-23",
        "4. Output Size": "Compact",
        "5. Time Zone": "US/Eastern"
    },
    "Time Series (Daily)": {
        "2026-01-23": {
            "1. open": "294.0700",
            "2. high": "294.3350",
            "3. low": "289.7900",
            "4. close": "292.4400",
            "5. volume": "3298424"
        },
        "2026-01-22": {
            "1. open": "299.4200",
            "2. high": "300.9300",
            "3. low": "293.5300",
            "4. close": "294.6700",
            "5. volume": "3670152"
        }
    }
}"""


def test1(prices):
    group_keys = itemgetter(0, 1)

    sorted_data = sorted(prices, key=group_keys)

    grouped_data = itertools.groupby(sorted_data, key=group_keys)

    df = pd.DataFrame(grouped_data)

    print(df)

    for key, group in grouped_data:
        for item in list(group):
            print(item)


def test2(prices):
    df = pd.DataFrame(prices)

    pivoted = df.pivot(
        index=[df.columns[0], df.columns[1]],
        columns=df.columns[2],
        values=df.columns[3],
    )
    # print(pivoted)
    for index, row in pivoted.iterrows():
        # print(f"Row index: {index}, Value 1: {row.iloc[0]} Value 2: {row['2. high']}")
        yield prc.Price(
            index[0],
            row["1. open"],
            row["2. high"],
            row["3. low"],
            row["4. close"],
            row["5. volume"],
            index[1],
        )


def test3():
    prices = jtp.parse(json.loads(json_data))
    price_list = test2(prices)

    for p in price_list:
        print(p)


def test4():
    prices = jtp.parse2(json.loads(json_data))

    for p in prices:
        print(p)


if __name__ == "__main__":
    test4()
