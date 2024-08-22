from typing import List
from services.payment.helpers.payment_helper import PaymentHelper
from services.payment.models.create_payment_dto import CreatePaymentDto
from services.payment.models.payment_registry_response import PaymentRegistryResponse
from services.payment.models.payment_response import PaymentResponse
from utilities.api_utilities import ApiUtilities


class PaymentService:
    def __init__(self, api_utils: ApiUtilities):
        self.api_utils = api_utils
        self.payment_helper = PaymentHelper(api_utils)

    def update_api_utils(self, token):
        self.api_utils.update_headers(headers={"Authorization": f"Bearer {token}"})

    def post_create(self, create_payment_dto: CreatePaymentDto) -> PaymentRegistryResponse:
        response = self.payment_helper.post_create(
            json=create_payment_dto.model_dump(by_alias=True, exclude_defaults=True))
        return PaymentRegistryResponse(**response.json())

    def get_user(self) -> List[PaymentResponse]:
        response = self.payment_helper.get_user()
        return [PaymentResponse(**payment) for payment in response.json()]

    def get_user_id(self, user_id) -> List[PaymentResponse]:
        response = self.payment_helper.get_user_id(user_id=user_id)
        return [PaymentResponse(**payment) for payment in response.json()]
