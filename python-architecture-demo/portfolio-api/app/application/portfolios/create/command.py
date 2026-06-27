from pydantic import BaseModel, Field


class CreatePortfolioCommand(BaseModel):
    """
    Request object for the Create Portfolio use case.
    """

    name: str = Field(
        min_length=1,
        max_length=100,
        description="Portfolio name",
    )
