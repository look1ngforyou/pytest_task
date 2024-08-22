from pydantic import BaseModel, Field
from uuid import UUID
from typing import List, Optional
import datetime
from utilities.roles_enumeration import RolesEnumeration


class UserResponse(BaseModel):
    id: UUID
    email: str
    full_name: str = Field(alias="fullName")
    roles: List[RolesEnumeration]
    verified: Optional[bool] = None
    created_at: Optional[datetime.datetime] = Field(alias="createdAt", default=None)
    banned: Optional[bool] = None
