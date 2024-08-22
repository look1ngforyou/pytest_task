from faker import Faker
from config.config import Configuration
import pytest
import requests
from services.movies.helpers.genre_helper import GenreHelper
from logger.logger import Logger
from services.movies.models.genre import Genre

faker = Faker()


class TestGenreCreateContract:
    def test_genre_create_anonym_contract(self, super_admin_movie_api_utilities):
        Logger.info("Create new genre")
        genre_helper = GenreHelper(super_admin_movie_api_utilities)
        genre = Genre(name=faker.name())
        response = genre_helper.post_genre(genre.model_dump())

        actual_status_code = response.status_code
        expected_status_code = requests.status_codes.codes.created

        assert actual_status_code == expected_status_code, \
            f"Expected status code: {expected_status_code}, got instead status code: {actual_status_code}"
