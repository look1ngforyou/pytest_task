from pydantic import BaseModel, Field, ConfigDict
from services.payment.payment_model.card_dto import CardDto


class CreatePaymentDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    movie_id: int = Field(alias="movieId")
    amount: int
    card: CardDto
