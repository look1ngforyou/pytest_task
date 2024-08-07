from services.movies.helpers.genre_helper import GenreHelper
from services.movies.helpers.movies_helper import MoviesHelper
from services.movies.models.create_genre_dto import CreateGenreDto
from services.movies.models.create_movie_dto import CreateMovieDto
from services.movies.models.genre_response import GenreResponse
from services.movies.models.movie_response import MovieResponse


class MoviesService:
    SERVICE_URL = "https://api.dev-cinescope.store"

    def __init__(self, api_utils):
        self.api_utils = api_utils

        self.genre_helper = GenreHelper(self.api_utils)
        self.movies_helper = MoviesHelper(self.api_utils)

    def post_genre(self, create_genre: CreateGenreDto):
        response = self.genre_helper.post_genre(json=create_genre.model_dump(by_alias=True,
                                                                             exclude_defaults=True))
        return GenreResponse(**response.json())

    def post_movie(self, create_movie: CreateMovieDto):
        response = self.movies_helper.post_movie(create_movie.model_dump(by_alias=True,
                                                                         exclude_defaults=True))
        return MovieResponse(**response.json())

    def post_genre_and_movie(self):
        raise NotImplementedError

    def post_random_genre(self):
        raise NotImplementedError
