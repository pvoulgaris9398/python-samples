# pylint: disable=[missing-module-docstring]
import datetime
import pandas as pd
import yfinance as yf

# Working through:
# https://builtin.com/data-science/portfolio-optimization-python

# https://algotrading101.com/learn/yfinance-guide/
# https://pypi.org/project/yfinance/
def get_monthly_stock_price_data(tickers, start, end):
    data = yf.download(tickers, start, end, interval = "1mo")
    return data

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

start = datetime.datetime(2020, 1, 1)
end = datetime.datetime(2025, 1, 1)

tickers = ["PFE", "JNJ", "MSFT", "AAPL"]

prices = get_monthly_stock_price_data(tickers, start, end)

print(prices)

