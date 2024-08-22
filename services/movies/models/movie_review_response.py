import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict


class User(BaseModel):
    full_name: str = Field(alias="fullName")


class MovieReviewResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True
    )
    user_id: str = Field(alias="userId")
    rating: int = Field(ge=0, le=5)
    text: str
    hidden: Optional[bool] = None
    created_at: datetime.datetime = Field(alias="createdAt")
    user: User
