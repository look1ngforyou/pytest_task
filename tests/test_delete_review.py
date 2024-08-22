import random
import pytest
import requests.status_codes
from faker import Faker
from pydantic import ValidationError

from logger.logger import Logger
from services.movies.helpers.review_helper import ReviewHelper
from services.movies.models.create_movie_dto import CreateMovieDto, LocationEnum
from services.movies.models.create_genre_dto import CreateGenreDto
from services.movies.models.movie_review import MovieReview

faker = Faker()


class TestDeleteReview:
    def test_create_movie_make_delete_review(self, super_admin_movie_api_service, super_admin_payment_api_utilities,
                                             create_new_movie):
        Logger.info("Step 1 - Create a new movie")
        created_movie = create_new_movie()

        Logger.info("Step 2 - Make a review")
        movie_review = MovieReview(rating=random.randint(1, 5), text=faker.pystr())
        post_movie_review = super_admin_movie_api_service.post_movie_review(movie_id=created_movie.id,
                                                                            movie_review=movie_review)
        Logger.info("Step 3 - Delete a movie review")
        super_admin_movie_api_service.delete_review(created_movie.id)

        review_helper = ReviewHelper(super_admin_payment_api_utilities)
        response = review_helper.patch_movie_review(movie_id=created_movie.id, user_id=post_movie_review.user_id)

        actual_status_code = response.status_code
        expected_status_code = requests.status_codes.codes.not_found

        assert actual_status_code == expected_status_code, \
            f"Expected status code: {expected_status_code}, got instead status code: {actual_status_code}"