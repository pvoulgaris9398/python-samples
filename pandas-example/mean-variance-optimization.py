# pylint: disable=[missing-module-docstring]
from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt.expected_returns import mean_historical_return

# rom pypfopt.risk_models import CovarianceShrinkage
from sklearn.covariance import EmpiricalCovariance

# from sklearn.covariance import EmpiricalCovariance
import prices

# Working through:
# Mean Variance Optimization Example from:
# https://builtin.com/data-science/portfolio-optimization-python

# Build portfolio
portfolio = prices.build_portfolio()

# https://pyportfolioopt.readthedocs.io/en/latest/
mu = mean_historical_return(portfolio)

# https://scikit-learn.org/stable/
# S = CovarianceShrinkage(portfolio).ledoit_wolf()

S = EmpiricalCovariance(portfolio)

ef = EfficientFrontier(mu, S)

ef.add_constraint(lambda x: x[0] == 0.02)

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
