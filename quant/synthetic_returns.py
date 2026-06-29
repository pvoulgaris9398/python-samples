"""Helpers for generating synthetic asset return series for quantitative examples."""

from __future__ import annotations

import random


def build_synthetic_returns(
    num_assets: int = 100,
    days: int = 250,
    seed: int = 42,
    market_mean: float = 0.0004,
    market_vol: float = 0.012,
    beta_range: tuple[float, float] = (0.35, 1.2),
    idiosyncratic_vol_range: tuple[float, float] = (0.008, 0.018),
    stress_days: set[int] | None = None,
    stress_size_range: tuple[float, float] = (0.02, 0.04),
    stress_scale_even: float = 1.0,
    stress_scale_odd: float = 0.7,
) -> list[list[float]]:
    """Create synthetic return series for a portfolio of assets.

    The simulation uses a common market factor plus asset-specific noise,
    which makes it suitable for toy portfolio risk, optimization, and
    performance samples.
    """
    if num_assets <= 0:
        raise ValueError("num_assets must be positive")
    if days <= 0:
        raise ValueError("days must be positive")

    rng = random.Random(seed)
    if stress_days is None:
        stress_days = {20, 84, 140, 207}

    market_factor = [rng.gauss(market_mean, market_vol) for _ in range(days)]
    asset_returns: list[list[float]] = []

    for asset_index in range(num_assets):
        beta = rng.uniform(*beta_range)
        idiosyncratic_vol = rng.uniform(*idiosyncratic_vol_range)
        series: list[float] = []

        for day_index, factor in enumerate(market_factor):
            shock = rng.gauss(0.0, idiosyncratic_vol)
            if day_index in stress_days:
                stress_scale = (
                    stress_scale_even if asset_index % 2 == 0 else stress_scale_odd
                )
                shock -= rng.uniform(*stress_size_range) * stress_scale
            series.append(beta * factor + shock)

        asset_returns.append(series)

    return asset_returns
