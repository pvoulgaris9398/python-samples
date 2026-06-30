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
from pathlib import Path
from statistics import NormalDist, mean, pstdev

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

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


def rolling_historical_var(
    returns: list[float],
    confidence: float,
    portfolio_value: float,
    window: int = 30,
    horizon_days: int = 1,
) -> list[float]:
    """Compute a rolling historical VaR series for a return series."""
    if window <= 0:
        raise ValueError("window must be positive")

    rolling_values: list[float] = []
    for index in range(len(returns)):
        window_returns = returns[max(0, index - window + 1) : index + 1]
        if len(window_returns) < 2:
            rolling_values.append(float("nan"))
        else:
            rolling_values.append(
                historical_var(
                    window_returns, confidence, portfolio_value, horizon_days
                )
            )
    return rolling_values


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

    histogram_path = Path(__file__).resolve().parent / "var_return_histogram.png"
    fig, ax = plt.subplots(figsize=(8, 4))  # type: ignore
    ax.hist(portfolio, bins=30, alpha=0.8, color="steelblue", edgecolor="black")  # type: ignore
    ax.axvline(  # type: ignore
        percentile(portfolio, 1 - confidence_levels[0]),
        color="crimson",
        linestyle="--",
        label=f"{confidence_levels[0]:.0%} historical VaR threshold",
    )
    ax.set_title("Distribution of Daily Portfolio Returns")  # type: ignore
    ax.set_xlabel("Daily Return")  # type: ignore
    ax.set_ylabel("Frequency")  # type: ignore
    ax.grid(alpha=0.25)  # type: ignore
    ax.legend()  # type: ignore
    fig.tight_layout()
    fig.savefig(histogram_path, dpi=200)  # type: ignore
    plt.close(fig)
    print(f"Saved return histogram to {histogram_path}")

    rolling_window = 30
    rolling_var_values = rolling_historical_var(
        portfolio,
        confidence=0.95,
        portfolio_value=portfolio_value,
        window=rolling_window,
    )
    rolling_path = Path(__file__).resolve().parent / "rolling_var.png"
    fig, ax = plt.subplots(figsize=(8, 4))  # type: ignore
    ax.plot(  # type: ignore
        range(1, len(portfolio) + 1), rolling_var_values, color="crimson", linewidth=1.5
    )
    ax.set_title(f"Rolling {rolling_window}-Day Historical VaR at 95% Confidence")  # type: ignore
    ax.set_xlabel("Day")  # type: ignore
    ax.set_ylabel("VaR ($)")  # type: ignore
    ax.set_ylim(bottom=0)
    ax.grid(alpha=0.25)  # type: ignore
    fig.tight_layout()
    fig.savefig(rolling_path, dpi=200)  # type: ignore
    plt.close(fig)
    print(f"Saved rolling VaR chart to {rolling_path}")

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
