import requests
from faker import Faker
from logger.logger import Logger
import pytest
from services.authorization.helpers.authorization_helper import AuthorizationHelper
from services.authorization.models.login_dto import LoginDto
from services.authorization.models.register_dto import RegisterDto

faker = Faker()


class TestRegisterUser:
    def test_register_user_anonym_contract(self, anonymous_auth_api_utilities):
        authorization_helper = AuthorizationHelper(anonymous_auth_api_utilities)
        user_email = faker.email()
        user_password = faker.password(length=8, special_chars=False)
        register_dto = RegisterDto(email=user_email,
                                   fullName=faker.first_name() + " " + faker.last_name(),
                                   password=user_password,
                                   passwordRepeat=user_password
                                   )
        authorization_helper.post_register_user(json=register_dto.model_dump(by_alias=True))

        login_dto = LoginDto(email=user_email, password=user_password)
        login_response = authorization_helper.post_login_user(json=login_dto.model_dump())

        actual_status_code = login_response.status_code
        expected_status_code = requests.status_codes.codes.ok

        assert actual_status_code == expected_status_code, \
            f"Expected status code: {expected_status_code}, got instead status code: {actual_status_code}"

