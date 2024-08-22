import datetime
from typing import List
from pydantic import BaseModel, Field
from utilities.roles_enumeration import RolesEnumeration


class EditingUserRealResponse(BaseModel):
    email: str
    full_name: str = Field(alias="fullName")
    verified: bool
    banned: bool
    roles: List[RolesEnumeration]
    created_at: datetime.datetime = Field(alias="createdAt", default=None)