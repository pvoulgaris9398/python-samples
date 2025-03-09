# pylint: disable=[missing-module-docstring]
import pandas as pd

data = {"name": ["bread", "carrots", "apples"], "price": [101, 202, 303]}

df = pd.DataFrame(data)

print(df.info())


def combine_stocks(tickers, start, end):
    data_frames = []
    for i in tickers:
        data_frames.append(prices.get_stock_price_data(i, start, end))

    df_merged = reduce(
        lambda left, right: pd.merge(left, right, on=["Date"], how="outer"), data_frames
    )
    return df_merged
