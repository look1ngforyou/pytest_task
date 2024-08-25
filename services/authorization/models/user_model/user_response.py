from pydantic import BaseModel, Field, ConfigDict
from uuid import UUID
from typing import List, Optional
import datetime
from services.authorization.models.roles_enumeration import RolesEnumeration


class UserResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID
    email: str
    full_name: str = Field(alias="fullName")
    roles: List[RolesEnumeration]
    verified: Optional[bool] = None
    created_at: Optional[datetime.datetime] = Field(alias="createdAt", default=None)
    banned: Optional[bool] = None
