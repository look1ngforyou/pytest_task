from utils.api_utils import ApiUtils


class UserHelper:
    USER_ENDPOINT = "/user"

    def __init__(self, api_utils: ApiUtils):
        self.api_utils = api_utils

    def get_users(self):
        response = self.api_utils.get(self.USER_ENDPOINT)
        return response
