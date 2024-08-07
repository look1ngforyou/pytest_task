import os

import pytest

from services.auth.auth_api_service import AuthService
from services.auth.models.login_dto import LoginDto
from services.movies.movies_api_service import MoviesService
from utils.api_utils import ApiUtils


@pytest.fixture(scope="session", autouse=False)
def api_utils_anonym_auth():
    api_utils_anonym = ApiUtils(url=AuthService.SERVICE_URL)
    yield api_utils_anonym


@pytest.fixture(scope="session", autouse=False)
def api_utils_super_admin_api(api_utils_anonym_auth):
    email = os.environ["USER_EMAIL"]
    password = os.environ["USER_PASSWORD"]

    auth_service = AuthService(api_utils=api_utils_anonym_auth)
    login_user = LoginDto(email=email, password=password)
    login_response = auth_service.login_user(login_user)

    api_utils_super_admin = ApiUtils(url=AuthService.SERVICE_URL,
                                     headers={"Authorization": f"Bearer {login_response.access_token}"})
    yield api_utils_super_admin


@pytest.fixture(scope="session", autouse=False)
def api_service_anonym_api(api_utils_anonym_auth):
    api_service = MoviesService(api_utils=api_utils_anonym_auth)
    yield api_service


@pytest.fixture(scope="session", autouse=False)
def api_service_super_admin_api(api_utils_super_admin_api):
    api_service = MoviesService(api_utils=api_utils_super_admin_api)
    yield api_service
