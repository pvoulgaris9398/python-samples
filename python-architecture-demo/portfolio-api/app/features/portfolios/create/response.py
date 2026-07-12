from uuid import UUID

from pydantic import BaseModel, ConfigDict


class CreatePortfolioResponse(BaseModel):
    """
    Response returned by the Create Portfolio use case.
    """

    model_config = ConfigDict(
        frozen=True,
    )

    id: UUID
    name: str
