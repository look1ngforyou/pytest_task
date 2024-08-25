from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
from services.movies.models.genre_model.genre import Genre
from services.movies.models.location_enumeration import LocationEnum


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
    rating: int = Field(ge=0, le=5)
