from pydantic import BaseModel, Field


class MovieReview(BaseModel):
    rating: int = Field(ge=0, le=5)
    text: str
