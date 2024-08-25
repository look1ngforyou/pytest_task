from typing import List
from pydantic import BaseModel
from services.authorization.models.roles_enumeration import RolesEnumeration


class EditUserDto(BaseModel):
    roles: List[RolesEnumeration]
    verified: bool
    banned: bool

