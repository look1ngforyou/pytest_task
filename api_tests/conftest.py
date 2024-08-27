import os
import random
import pytest
from services.authorization.authorization_api_service import AuthorizationService
from services.authorization.models.authorization_model.login_dto import LoginDto
from services.authorization.models.authorization_model.register_dto import RegisterDto
from services.movies.models.movie_model.create_movie_dto import CreateMovieDto
from services.payment.payment_service import PaymentService
from utilities.api_utilities import ApiUtilities
from config.config import Configuration
from faker import Faker
from collections import namedtuple

from services.movies.models.location_enumeration import LocationEnum

email = os.environ["USER_EMAIL"]
password = os.environ["USER_PASSWORD"]
faker = Faker()


@pytest.fixture(scope="session", autouse=False)
def auth_api_utilities():
    anonymous_api_utils = ApiUtilities(Configuration.AUTH_SERVICE_URL)
    yield anonymous_api_utils


@pytest.fixture(scope="session", autouse=False)
def super_admin_auth_api_utilities(auth_api_utilities):
    auth_service = AuthorizationService(api_utils=auth_api_utilities)
    login_dto = LoginDto(email=email, password=password)
    login_response = auth_service.login_user(login_dto)

    api_utils_super_admin = ApiUtilities(Configuration.AUTH_SERVICE_URL, headers={
        "Authorization": f"Bearer {login_response.access_token}"})

    yield api_utils_super_admin


@pytest.fixture(scope="session", autouse=False)
def auth_api_service(super_admin_auth_api_utilities):
    api_service = AuthorizationService(super_admin_auth_api_utilities)
    yield api_service


@pytest.fixture(scope="function")
def register_user(auth_api_service):
    auth_api_service.update_api_utils(token=None)
    RegisteredUser = namedtuple('RegisteredUser', ['user', 'password', 'email'])
    user_email = faker.email()
    user_password = faker.password(length=8, special_chars=False)
    register_dto = RegisterDto(email=user_email,
                               full_name=faker.first_name() + " " + faker.last_name(),
                               password=user_password,
                               password_repeat=user_password
                               )
    registered_user = auth_api_service.register_user(register_dto=register_dto)
    yield RegisteredUser(user=registered_user, password=user_password, email=user_email)


@pytest.fixture(scope="function")
def create_new_movie(movie_api_service):
    def _create_movie(genre_id=None):

        if genre_id is not None:
            movie = CreateMovieDto(name=faker.name(),
                                   price=random.randint(500, 1000),
                                   description=faker.pystr(),
                                   location=random.choice(list(LocationEnum)),
                                   published=True,
                                   genre_id=genre_id,
                                   image_url=faker.url())

        else:
            genres = movie_api_service.get_genres()
            selected_genre = random.choice(genres.genres)

            movie = CreateMovieDto(name=faker.name(),
                                   price=random.randint(500, 1000),
                                   description=faker.pystr(),
                                   location=random.choice(list(LocationEnum)),
                                   published=True,
                                   genre_id=selected_genre.id,
                                   image_url=faker.url())

        created_movie = movie_api_service.post_movie(movie)
        return created_movie

    return _create_movie
