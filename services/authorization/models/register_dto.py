from pydantic import BaseModel, Field


class RegisterDto(BaseModel):
    email: str
    full_name: str = Field(alias="fullName")
    password: str
    password_repeat: str = Field(alias="passwordRepeat")

