import pytest
import requests
from faker import Faker
from services.authorization.helpers.authorization_helper import AuthorizationHelper
from logger.logger import Logger
from services.authorization.models.login_dto import LoginDto

faker = Faker()


class TestDeleteUser:
    def test_register_and_delete_user(self, anonymous_user_auth_api_service, anonymous_auth_api_utilities,
                                      register_user):
        Logger.info("Step 1 - Register new user")
        registered_user_info = register_user

        registered_user = registered_user_info.user
        password = registered_user_info.password
        email = registered_user_info.email

        Logger.info("Step 2 - Log in as new user")
        login_dto = LoginDto(email=email, password=password)
        login_response = anonymous_user_auth_api_service.login_user(login_dto=login_dto)

        Logger.info("Step 3 - Delete new user")
        anonymous_user_auth_api_service.update_api_utils(token=login_response.access_token)
        anonymous_user_auth_api_service.delete_user(registered_user.id)

        Logger.info("Step 4 - Log in as new user for confirm")
        auth_helper = AuthorizationHelper(anonymous_auth_api_utilities)
        login_response = auth_helper.post_login_user(json=login_dto.model_dump(by_alias=True, exclude_defaults=True))

        actual_status_code = login_response.status_code
        expected_status_code = requests.status_codes.codes.unauthorized

        assert actual_status_code == expected_status_code, \
            f"Expected status code: {expected_status_code}, got instead status code: {actual_status_code}"