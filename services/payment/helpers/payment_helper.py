import requests
from utilities.api_utilities import ApiUtilities


class PaymentHelper:
    PAYMENT_ENDPOINT = "/create"
    USER_ENDPOINT = "/user/"

    def __init__(self, api_utilities: ApiUtilities):
        self.api_utilities = api_utilities

    def post_create(self, json) -> requests.Response:
        response = self.api_utilities.post(self.PAYMENT_ENDPOINT, json=json)
        return response

    def get_user_id(self, user_id) -> requests.Response:
        response = self.api_utilities.get(self.USER_ENDPOINT + str(user_id))
        return response

    def get_user(self) -> requests.Response:
        response = self.api_utilities.get(self.USER_ENDPOINT)
        return response
