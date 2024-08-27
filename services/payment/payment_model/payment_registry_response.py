from services.payment.payment_model.status_enumeration import Status
from pydantic import BaseModel


class PaymentRegistryResponse(BaseModel):
    status: Status
