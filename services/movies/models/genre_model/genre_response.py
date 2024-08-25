from typing import List
from pydantic import BaseModel


class GenreResponse(BaseModel):
    id: int
    name: str


class GenreListResponse(BaseModel):
    genres: List[GenreResponse]
