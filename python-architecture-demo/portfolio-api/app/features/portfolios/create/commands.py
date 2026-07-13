from uuid import UUID

from pydantic import BaseModel, Field


class CreatePortfolioResponse(BaseModel):
    id: UUID
    name: str


class CreatePortfolioRequest(BaseModel):
    """
    Request object for the Create Portfolio use case.
    """

    name: str = Field(
        min_length=1,
        max_length=100,
        description="Portfolio name",
    )
