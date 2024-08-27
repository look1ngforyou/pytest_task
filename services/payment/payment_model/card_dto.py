from pydantic import BaseModel, Field, ConfigDict


class CardDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    card_number: str = Field(alias="cardNumber")
    card_holder: str = Field(alias="cardHolder")
    expiration_date: str = Field(alias="expirationDate")
    security_code: int = Field(alias="securityCode")
