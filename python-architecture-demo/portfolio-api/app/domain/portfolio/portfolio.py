from sqlalchemy import UUID


@dataclass
class Portfolio:
    id: UUID
    name: str
    positions: list[Position]

    def add_position(self, position: Position) -> None: ...
