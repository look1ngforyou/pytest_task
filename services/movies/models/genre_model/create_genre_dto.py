from pydantic import BaseModel


class CreateGenreDto(BaseModel):
    name: str
