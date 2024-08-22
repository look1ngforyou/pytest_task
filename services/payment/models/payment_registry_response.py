from enum import Enum
from utilities.status_enumeration import Status
from pydantic import BaseModel


class PaymentRegistryResponse(BaseModel):
    status: Status
