# pylint: disable=[missing-module-docstring]
import prices
from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices
from pypfopt import HRPOpt

# Working through:
# Hierarchical Risk Party (HRP) Example from:
# https://builtin.com/data-science/portfolio-optimization-python

portfolio = prices.build_portfolio()

returns = portfolio.pct_change().dropna()

hrp = HRPOpt(returns)

hrp_weights = hrp.optimize()

hrp.portfolio_performance(verbose=True)

latest_prices = get_latest_prices(portfolio)

da_hrp = DiscreteAllocation(hrp_weights, latest_prices, total_portfolio_value=100000)

allocation, leftover = da_hrp.greedy_portfolio()

print(dict(hrp_weights))

print("Discrete Allocation:", allocation)

print("Funds remaining: ${:.2f}".format(leftover))
