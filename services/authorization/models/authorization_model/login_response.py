from pydantic import BaseModel, Field, ConfigDict
from services.authorization.models.user_model.user_response import UserResponse
from typing import Optional


class LoginResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    user: UserResponse
    access_token: str = Field(alias="accessToken")
    refresh_token: Optional[str] = Field(alias="refreshToken")
    expires_in: int = Field(alias="expiresIn")