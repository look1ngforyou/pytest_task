from datetime import datetime
from ipaddress import IPv4Address
from typing import List
from uuid import UUID

from pydantic import BaseModel, Field


class UserResponse(BaseModel):
    id: UUID
    email: str
    full_name: str = Field(alias="fullName")
    roles: List[str]
    verified: bool
    created_at: datetime = Field(alias="createdAd")
    banned: bool
