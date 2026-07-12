from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Position:
    symbol: str

    quantity: Decimal
