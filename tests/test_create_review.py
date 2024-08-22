import random
import pytest
from faker import Faker
from logger.logger import Logger
from services.movies.models.create_movie_dto import CreateMovieDto, LocationEnum
from services.movies.models.create_genre_dto import CreateGenreDto
from services.movies.models.movie_review import MovieReview

faker = Faker()


class TestCreateReview:
    def test_create_genre_for_movie_and_make_review(self, super_admin_movie_api_service, create_new_movie):
        Logger.info("Step 1 - Create a new genre")
        genre = CreateGenreDto(name=faker.name())
        created_genre = super_admin_movie_api_service.post_genre(genre)

        Logger.info("Step 2 - Create a new movie")
        created_movie = create_new_movie(created_genre.id)

        Logger.info("Step 3 - Make a review")
        movie_review = MovieReview(rating=random.randint(1, 5), text=faker.pystr())
        post_movie_review = super_admin_movie_api_service.post_movie_review(movie_id=created_movie.id,
                                                                            movie_review=movie_review)

        Logger.info("Step 4 - Check movie review")
        movie_review = super_admin_movie_api_service.patch_movie_review(user_id=post_movie_review.user_id,
                                                                        movie_id=created_movie.id)

        assert movie_review.text == post_movie_review.text, \
            f"Expected review text {post_movie_review.text} got {movie_review.text} instead"

        assert movie_review.rating == post_movie_review.rating, \
            f"Expected review rating: {post_movie_review.text} got: {movie_review.text} instead"

    def test_choose_genre_for_movie_and_make_review(self, super_admin_movie_api_service, create_new_movie):
        Logger.info("Step 1 - Create a new movie")
        created_movie = create_new_movie()

        Logger.info("Step 2 - Make a review")
        movie_review = MovieReview(rating=random.randint(1, 5), text=faker.pystr())
        post_movie_review = super_admin_movie_api_service.post_movie_review(movie_id=created_movie.id,
                                                                            movie_review=movie_review)
        Logger.info("Step 3 - Check a movie review")
        assert movie_review.text == post_movie_review.text, \
            f"Expected review text {post_movie_review.text} got {movie_review.text} instead"

        assert movie_review.rating == post_movie_review.rating, \
            f"Expected review rating: {post_movie_review.text} got: {movie_review.text} instead"


