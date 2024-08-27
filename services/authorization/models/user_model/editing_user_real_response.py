import datetime
from typing import List
from pydantic import BaseModel, Field, ConfigDict
from services.authorization.models.roles_enumeration import RolesEnumeration


class EditingUserRealResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    email: str
    full_name: str = Field(alias="fullName")
    verified: bool
    banned: bool
    roles: List[RolesEnumeration]
    created_at: datetime.datetime = Field(alias="createdAt", default=None)