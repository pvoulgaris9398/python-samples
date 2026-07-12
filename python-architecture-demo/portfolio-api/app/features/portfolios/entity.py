from dataclasses import dataclass, field
from decimal import Decimal
from uuid import UUID

from .position import Position


@dataclass
class Portfolio:
    id: UUID

    name: str

    positions: list[Position] = field(default_factory=list)

    def add_position(self, position: Position):
        if any(p.symbol == position.symbol for p in self.positions):
            raise ValueError("Duplicate symbol.")

        self.positions.append(position)

    def market_value(self, prices: dict[str, Decimal]) -> Decimal:
        total = Decimal("0")

        for position in self.positions:
            total += position.quantity * prices[position.symbol]

        return total
