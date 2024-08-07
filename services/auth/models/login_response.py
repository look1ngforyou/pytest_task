from pydantic import BaseModel, Field, ConfigDict

from services.auth.models.user_response import UserResponse


class LoginResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    user: UserResponse
    access_token: str = Field(alias="accessToken")
    expires_in: int = Field(alias="expiresIn")
