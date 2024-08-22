from uuid import UUID
from pydantic import BaseModel, Field
from utilities.status_enumeration import Status


class PaymentResponse(BaseModel):
    id: int
    user_id: UUID = Field(alias="userId")
    movie_id: int = Field(alias="movieId")
    total: int
    amount: int
    created_at: str = Field(alias="createdAt")
    status: Status
