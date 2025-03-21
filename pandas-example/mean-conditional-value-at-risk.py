# pylint: disable=[missing-module-docstring]
from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices
from pypfopt.efficient_frontier import EfficientCVaR
from pypfopt.expected_returns import mean_historical_return

import prices

# Working through:
# Mean Conditional Value at Risk Example from:
# https://builtin.com/data-science/portfolio-optimization-python

portfolio = prices.build_portfolio()
mu = mean_historical_return(portfolio)
S = portfolio.cov()

ef_cvar = EfficientCVaR(mu, S)

cvar_weights = ef_cvar.min_cvar()

cleaned_weights = ef_cvar.clean_weights()

# ef_cvar.portfolio_performance(verbose=True)

latest_prices = get_latest_prices(portfolio)

da_cvar = DiscreteAllocation(cvar_weights, latest_prices, total_portfolio_value=100000)

allocation, leftover = da_cvar.greedy_portfolio()

print(dict(cvar_weights))

print("Discrete Allocation:", allocation)

print("Funds remaining: ${:.2f}".format(leftover))
