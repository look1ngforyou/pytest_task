from enum import Enum
from typing import Optional, Union

from pydantic import BaseModel, Field, ConfigDict


class LocationEnum(str, Enum):
    SPB = "SPB"
    MSK = "MSK"


class CreateMovieDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str
    image_url: str = Field(alias="imageUrl", default=None)
    price: float
    description: str
    location: LocationEnum
    published: bool
    genre_id: int = Field(alias="genreId")