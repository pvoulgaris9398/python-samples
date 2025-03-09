# pylint: disable=[missing-module-docstring]
import pandas as pd
import yfinance as yf
from functools import reduce
from pypfopt.expected_returns import mean_historical_return
from pypfopt.risk_models import CovarianceShrinkage
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices

# Working through:
# Mean Variance Optimization Example from:
# https://builtin.com/data-science/portfolio-optimization-python


# https://algotrading101.com/learn/yfinance-guide/
# https://pypi.org/project/yfinance/
def get_stock_price_data(ticker, start, end):
    dat = yf.Ticker(ticker)
    data = dat.history(start=start, end=end, auto_adjust=False)
    data[f"{ticker}"] = data["Close"]
    data = data[[f"{ticker}"]]
    return data


def combine_stocks(tickers, start, end):
    data_frames = []
    for i in tickers:
        data_frames.append(get_stock_price_data(i, start, end))

    df_merged = reduce(
        lambda left, right: pd.merge(left, right, on=["Date"], how="outer"), data_frames
    )
    return df_merged


pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

start = "2019-09-15"
end = "2021-09-15"

tickers = [
    "MRNA",
    "PFE",
    "JNJ",
    "GOOGL",
    "META",  # "FB"
    "AAPL",
    "COST",
    "WMT",
    "KR",
    "JPM",
    "BAC",
    "HSBC",
]

portfolio = combine_stocks(tickers, start, end)

# https://pyportfolioopt.readthedocs.io/en/latest/
mu = mean_historical_return(portfolio)

# https://scikit-learn.org/stable/
S = CovarianceShrinkage(portfolio).ledoit_wolf()

ef = EfficientFrontier(mu, S)
weights = ef.max_sharpe()

cleaned_weights = ef.clean_weights()

ef.portfolio_performance(verbose=True)

latest_prices = get_latest_prices(portfolio)

da = DiscreteAllocation(weights, latest_prices, total_portfolio_value=100000)

allocation, leftover = da.greedy_portfolio()

# My numbers are pretty close to the author's
# Sharpe Ratio is almost spot-on, Expected return and Annual volatility are close
# except that for the Discrete Allocations: GOOGL seems way-off and KR is a little off

print(dict(cleaned_weights))

print("Discrete Allocation:", allocation)

print("Funds remaining: ${:.2f}".format(leftover))
