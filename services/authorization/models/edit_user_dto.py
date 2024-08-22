from typing import List
import pydantic
from pydantic import BaseModel
from utilities.roles_enumeration import RolesEnumeration


class EditUserDto(BaseModel):
    roles: List[RolesEnumeration]
    verified: bool
    banned: bool

