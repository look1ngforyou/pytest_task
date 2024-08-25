from uuid import UUID
from pydantic import BaseModel, Field, ConfigDict
from services.payment.payment_model.status_enumeration import Status


class PaymentResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int
    user_id: UUID = Field(alias="userId")
    movie_id: int = Field(alias="movieId")
    total: int
    amount: int
    created_at: str = Field(alias="createdAt")
    status: Status
