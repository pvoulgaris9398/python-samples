"""Simple VaR example for reviewing quantitative risk concepts.

This script illustrates three common ways to think about portfolio risk:
1. Parametric VaR (normal-distribution assumption)
2. Historical VaR (empirical distribution)
3. Expected Shortfall / CVaR (tail risk beyond VaR)

It uses a toy 100-asset portfolio with synthetic daily returns so you can
inspect how assumptions and sample behavior affect the risk estimate.
"""

from __future__ import annotations

import math
from statistics import NormalDist, mean, pstdev

try:
    from synthetic_returns import build_synthetic_returns
except ModuleNotFoundError:  # pragma: no cover - fallback for repo-root execution
    from quant.synthetic_returns import build_synthetic_returns


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


def portfolio_returns(
    asset_returns: list[list[float]], weights: list[float]
) -> list[float]:
    """Combine multiple asset return series into a portfolio return series."""
    if not asset_returns:
        raise ValueError("asset_returns cannot be empty")
    if len(asset_returns) != len(weights):
        raise ValueError("weights must match the number of assets")

    num_days = len(asset_returns[0])
    return [
        sum(
            weights[asset_index] * asset_returns[asset_index][day_index]
            for asset_index in range(len(weights))
        )
        for day_index in range(num_days)
    ]


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
    num_assets = 100
    days = 250
    confidence_levels = (0.95, 0.99)

    weights = [1.0 / num_assets for _ in range(num_assets)]
    asset_returns = build_synthetic_returns(
        num_assets=num_assets,
        days=days,
        seed=42,
        market_mean=0.0004,
        market_vol=0.012,
        beta_range=(0.35, 1.2),
        idiosyncratic_vol_range=(0.008, 0.018),
    )
    portfolio = portfolio_returns(asset_returns, weights)

    print("Simple VaR example for a 100-asset portfolio")
    print("=" * 44)
    print(f"Portfolio value: ${portfolio_value:,.0f}")
    print(f"Number of assets: {num_assets}")
    print("Equal-weighted portfolio")
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
