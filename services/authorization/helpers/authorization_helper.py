import requests
from utilities.api_utilities import ApiUtilities


class AuthorizationHelper:
    REGISTER_ENDPOINT = '/register'
    LOGIN_ENDPOINT = '/login'

    def __init__(self, api_utilities: ApiUtilities):
        self.api_utilities = api_utilities

    def post_register_user(self, json) -> requests.Response:
        response = self.api_utilities.post(self.REGISTER_ENDPOINT, json=json)
        return response

    def post_login_user(self, json) -> requests.Response:
        response = self.api_utilities.post(self.LOGIN_ENDPOINT, json=json)
        return response


