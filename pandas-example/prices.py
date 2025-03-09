import config
import yfinance as yf
import pandas as pd
from functools import reduce

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)


# https://algotrading101.com/learn/yfinance-guide/
# https://pypi.org/project/yfinance/
def get_stock_price_data(ticker, start, end):
    dat = yf.Ticker(ticker)
    data = dat.history(start=start, end=end, auto_adjust=False)
    data[f"{ticker}"] = data["Close"]
    data = data[[f"{ticker}"]]
    return data


def build_portfolio():
    data_frames = []
    for i in config.tickers:
        data_frames.append(get_stock_price_data(i, config.start, config.end))

    df_merged = reduce(
        lambda left, right: pd.merge(left, right, on=["Date"], how="outer"), data_frames
    )
    return df_merged
