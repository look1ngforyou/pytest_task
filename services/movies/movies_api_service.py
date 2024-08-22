from services.movies.helpers.genre_helper import GenreHelper
from services.movies.helpers.movies_helper import MovieHelper
from services.movies.helpers.review_helper import ReviewHelper
from services.movies.models.create_genre_dto import CreateGenreDto
from services.movies.models.create_movie_dto import CreateMovieDto
from services.movies.models.genre_response import GenreResponse, GenreListResponse
from services.movies.models.movie_response import MovieResponse
from services.movies.models.movie_review import MovieReview
from services.movies.models.movie_review_response import MovieReviewResponse
from utilities.api_utilities import ApiUtilities


class MoviesService:
    def __init__(self, api_utils: ApiUtilities):
        self.api_utils = api_utils
        self.genre_helper = GenreHelper(self.api_utils)
        self.movies_helper = MovieHelper(self.api_utils)
        self.review_helper = ReviewHelper(self.api_utils)

    def post_genre(self, create_genre: CreateGenreDto) -> GenreResponse:
        response = self.genre_helper.post_genre(json=create_genre.model_dump(by_alias=True,
                                                                             exclude_defaults=True))
        return GenreResponse(**response.json())

    def get_genres(self) -> GenreListResponse:
        response = self.genre_helper.get_genres()
        return GenreListResponse(genres=response.json())

    def post_movie(self, create_movie: CreateMovieDto) -> MovieResponse:
        response = self.movies_helper.post_movie(json=create_movie.model_dump(by_alias=True,
                                                                              exclude_defaults=True))
        return MovieResponse(**response.json())

    def post_movie_review(self, movie_id, movie_review: MovieReview) -> MovieReviewResponse:
        response = self.review_helper.post_movie_review(
            movie_id=movie_id, json=movie_review.model_dump(by_alias=True, exclude_defaults=True))
        return MovieReviewResponse(**response.json())

    def patch_movie_review(self, movie_id, user_id) -> MovieReviewResponse:
        response = self.review_helper.patch_movie_review(movie_id=movie_id, user_id=user_id)
        return MovieReviewResponse(**response.json())

    def delete_review(self, movie_id) -> MovieReviewResponse:
        response = self.review_helper.delete_review(movie_id=movie_id)
        return MovieReviewResponse(**response.json())
