from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ConfigDict


class LocationEnum(str, Enum):
    SPB = "SPB"
    MSK = "MSK"


class Genre(BaseModel):
    name: str


class MovieResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int
    name: str
    price: float
    description: str
    image_url: str = Field(alias="imageUrl", default=None)
    location: LocationEnum
    published: bool
    genre_id: int = Field(alias="genreId")
    genre: Genre
    created_at: datetime = Field(alias="createdAt")
    rating: float = Field(ge=0, le=5)