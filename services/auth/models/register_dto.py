from pydantic import Field, ConfigDict

from pydantic import BaseModel


class RegisterDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    email: str
    full_name: str = Field(alias="fullName")
    password: str
    password_repeat: str = Field(alias="passwordRepeat")
