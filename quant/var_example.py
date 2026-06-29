"""Simple VaR example for reviewing quantitative risk concepts.

This script illustrates three common ways to think about portfolio risk:
1. Parametric VaR (normal-distribution assumption)
2. Historical VaR (empirical distribution)
3. Expected Shortfall / CVaR (tail risk beyond VaR)

It uses a toy two-asset portfolio with synthetic daily returns so you can
inspect how assumptions and sample behavior affect the risk estimate.
"""

from __future__ import annotations

import math
import random
from statistics import NormalDist, mean, pstdev


def percentile(values: list[float], p: float) -> float:
    """Return the p-th percentile using linear interpolation."""
    if not values:
        raise ValueError("values cannot be empty")
    ordered = sorted(values)
    if len(ordered) == 1:
        return ordered[0]
    rank = (len(ordered) - 1) * p
    lower = math.floor(rank)
    upper = math.ceil(rank)
    if lower == upper:
        return ordered[lower]
    weight = rank - lower
    return ordered[lower] + (ordered[upper] - ordered[lower]) * weight


def build_synthetic_returns(seed: int = 42) -> tuple[list[float], list[float]]:
    """Create two correlated asset return series for demonstration."""
    rng = random.Random(seed)
    market_factor = [rng.gauss(0.0004, 0.012) for _ in range(250)]

    asset1: list[float] = []
    asset2: list[float] = []
    for i, factor in enumerate(market_factor):
        shock1 = rng.gauss(0.0, 0.011)
        shock2 = rng.gauss(0.0, 0.011)
        # Add a few stressed days to make tail risk visible.
        if i in {20, 84, 140, 207}:
            shock1 -= 0.035
            shock2 -= 0.028
        asset1.append(0.7 * factor + shock1)
        asset2.append(0.5 * factor + shock2)

    return asset1, asset2


def portfolio_returns(
    asset1: list[float], asset2: list[float], weights: tuple[float, float]
) -> list[float]:
    """Combine asset returns into a portfolio return series."""
    w1, w2 = weights
    return [w1 * r1 + w2 * r2 for r1, r2 in zip(asset1, asset2)]


def parametric_var(
    returns: list[float],
    confidence: float,
    portfolio_value: float,
    horizon_days: int = 1,
) -> float:
    """Parametric VaR assuming returns are approximately normal."""
    mu = mean(returns)
    sigma = pstdev(returns)
    alpha = 1 - confidence
    z_alpha = NormalDist().inv_cdf(alpha)
    return max(
        0.0,
        -((mu * math.sqrt(horizon_days)) + (z_alpha * sigma * math.sqrt(horizon_days)))
        * portfolio_value,
    )


def historical_var(
    returns: list[float],
    confidence: float,
    portfolio_value: float,
    horizon_days: int = 1,
) -> float:
    """Historical VaR from the empirical return distribution."""
    alpha = 1 - confidence
    q = percentile(returns, alpha)
    return max(0.0, -(q * math.sqrt(horizon_days)) * portfolio_value)


def expected_shortfall(
    returns: list[float],
    confidence: float,
    portfolio_value: float,
    horizon_days: int = 1,
) -> float:
    """Expected Shortfall (CVaR) for losses beyond the VaR threshold."""
    alpha = 1 - confidence
    threshold = percentile(returns, alpha)
    tail_returns = [r for r in returns if r <= threshold]
    if not tail_returns:
        return 0.0
    avg_tail = mean(tail_returns)
    return max(0.0, -(avg_tail * math.sqrt(horizon_days)) * portfolio_value)


def main() -> None:
    portfolio_value = 100_000.0
    weights = (0.6, 0.4)
    confidence_levels = (0.95, 0.99)

    asset1, asset2 = build_synthetic_returns(seed=42)
    portfolio = portfolio_returns(asset1, asset2, weights)

    print("Simple VaR example for a 2-asset portfolio")
    print("=" * 44)
    print(f"Portfolio value: ${portfolio_value:,.0f}")
    print(f"Weights: stock A={weights[0]:.0%}, stock B={weights[1]:.0%}")
    print(f"Average daily portfolio return: {mean(portfolio):.2%}")
    print(f"Daily volatility: {pstdev(portfolio):.2%}")
    print()

    for confidence in confidence_levels:
        parametric = parametric_var(portfolio, confidence, portfolio_value)
        historical = historical_var(portfolio, confidence, portfolio_value)
        cvar = expected_shortfall(portfolio, confidence, portfolio_value)

        print(f"Confidence level: {confidence:.0%}")
        print(f"  Parametric VaR: ${parametric:,.2f}")
        print(f"  Historical VaR: ${historical:,.2f}")
        print(f"  Expected Shortfall: ${cvar:,.2f}")
        print()

    print("Notes for review")
    print("- VaR is a loss estimate at a chosen confidence level and horizon.")
    print(
        "- Parametric VaR assumes returns are roughly normal and can understate tail risk."  # noqa: E501
    )
    print(
        "- Historical VaR uses observed returns and is simple, but it is sensitive to the sample history."  # noqa: E501
    )
    print(
        "- Expected Shortfall is often more informative because it looks at the average loss beyond the VaR cut-off."  # noqa: E501
    )
    print(
        "- In practice, portfolio risk also depends on correlations, time horizon, liquidity, and stress scenarios."  # noqa: E501
    )


if __name__ == "__main__":
    main()
