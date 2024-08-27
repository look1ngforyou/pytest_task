from pydantic import BaseModel, Field, ConfigDict


class RegisterDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    email: str
    full_name: str = Field(alias="fullName")
    password: str
    password_repeat: str = Field(alias="passwordRepeat")

