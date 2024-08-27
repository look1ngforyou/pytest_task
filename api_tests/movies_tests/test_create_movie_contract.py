import random
import requests.status_codes
from faker import Faker
from logger.logger import Logger
from services.movies.helpers.movies_helper import MovieHelper
from services.movies.models.location_enumeration import LocationEnum

faker = Faker()


class TestCreateMovieContract:
    def test_create_movie_admin_contract(self, movie_api_utilities):
        movie_helper = MovieHelper(movie_api_utilities)
        created_movie = movie_helper.post_movie(json={
            "name": faker.name(),
            "imageUrl": faker.url(),
            "price": random.randint(100, 1000),
            "description": faker.pystr(),
            "location": random.choice(list(LocationEnum)),
            "published": True,
            "genreId": random.randint(2, 6)
        })

        actual_status_code = created_movie.status_code
        expected_status_code = requests.status_codes.codes.created

        assert actual_status_code == expected_status_code, \
            f"Expected status code: {expected_status_code}, got instead status code: {actual_status_code}"
