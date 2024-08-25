import requests
from services.base_helper import BaseHelper
import json


class AuthorizationHelper(BaseHelper):
    REGISTER_ENDPOINT = 'register/'
    LOGIN_ENDPOINT = 'login/'

    def post_register_user(self, json: json) -> requests.Response:
        response = self.api_utilities.post(self.REGISTER_ENDPOINT, json=json)
        return response

    def post_login_user(self, json: json) -> requests.Response:
        response = self.api_utilities.post(self.LOGIN_ENDPOINT, json=json)
        return response
