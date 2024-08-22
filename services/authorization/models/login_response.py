from pydantic import BaseModel, Field
from pydantic import ConfigDict
from services.authorization.models.user_response import UserResponse
from typing import Optional


class LoginResponse(BaseModel):
    user: UserResponse
    access_token: str = Field(alias="accessToken")
    refresh_token: Optional[str] = Field(alias="refreshToken")
    expires_in: int = Field(alias="expiresIn")