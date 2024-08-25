from uuid import UUID
import requests
from services.base_helper import BaseHelper


class UserHelper(BaseHelper):
    USER_ENDPOINT = "user/"

    def get_user(self) -> requests.Response:
        response = self.api_utilities.get(self.USER_ENDPOINT)
        return response

    def delete_user(self, user_id: UUID) -> requests.Response:
        response = self.api_utilities.delete(self.USER_ENDPOINT + str(user_id))
        return response

    def patch_user(self, user_id: UUID, json) -> requests.Response:
        response = self.api_utilities.patch(self.USER_ENDPOINT + str(user_id), json=json)
        return response
