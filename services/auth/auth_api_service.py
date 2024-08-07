from services.auth.helpers.authorization_helper import AuthorizationHelper
from services.auth.helpers.user_helper import UserHelper
from services.auth.models.login_dto import LoginDto
from services.auth.models.login_response import LoginResponse


class AuthService:
    SERVICE_URL = "https://auth.dev-cinescope.store"

    def __init__(self, api_utils):
        self.api_utils = api_utils

        self.authorization_helper = AuthorizationHelper(self.api_utils)
        self.user_helper = UserHelper(self.api_utils)

    def login_user(self, login_dto: LoginDto):
        response = self.authorization_helper.login_user(json=login_dto.model_dump(by_alias=False,
                                                                                  exclude_defaults=True))
        return LoginResponse(**response.json())
