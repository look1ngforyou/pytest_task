import random

import pytest
from faker import Faker

from services.movies.models.location_enumeration import LocationEnum
from services.movies.models.movie_model.create_movie_dto import CreateMovieDto
from services.movies.movies_api_service import MoviesService
from services.payment.payment_service import PaymentService
from api_tests.conftest import email,password
from config.config import Configuration
from services.authorization.authorization_api_service import AuthorizationService
from services.authorization.models.authorization_model.login_dto import LoginDto
from utilities.api_utilities import ApiUtilities

faker = Faker()


@pytest.fixture(scope="session", autouse=False)
def movie_api_utilities(auth_api_utilities):
    auth_service = AuthorizationService(api_utils=auth_api_utilities)
    login_dto = LoginDto(email=email, password=password)
    login_response = auth_service.login_user(login_dto)

    api_utils_super_admin = ApiUtilities(Configuration.MOVIE_SERVICE_URL, headers={
        "Authorization": f"Bearer {login_response.access_token}"})

    yield api_utils_super_admin


@pytest.fixture(scope="session", autouse=False)
def movie_api_service(movie_api_utilities):
    api_service = MoviesService(movie_api_utilities)
    yield api_service





