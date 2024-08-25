import requests
from services.base_helper import BaseHelper
import json


class PaymentHelper(BaseHelper):
    PAYMENT_ENDPOINT = "create/"
    USER_ENDPOINT = "user/"

    def post_create(self, json: json) -> requests.Response:
        response = self.api_utilities.post(self.PAYMENT_ENDPOINT, json=json)
        return response

    def get_user_id(self, user_id: int) -> requests.Response:
        response = self.api_utilities.get(self.USER_ENDPOINT + str(user_id))
        return response

    def get_user(self) -> requests.Response:
        response = self.api_utilities.get(self.USER_ENDPOINT)
        return response
