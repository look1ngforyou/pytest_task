import random

from faker import Faker

from logger.logger import Logger
from services.movies.models.create_genre_dto import CreateGenreDto
from services.movies.models.create_movie_dto import CreateMovieDto, LocationEnum

faker = Faker()


class TestMovieCreate:
    def test_movie_create(self, api_service_super_admin_api):
        Logger.info("### Steps 1. Create genre")
        genre = CreateGenreDto(name=faker.name())
        created_genre = api_service_super_admin_api.post_genre(genre)
        movie = CreateMovieDto(name=faker.name(),
                               price=random.randint(100, 1000),
                               description=faker.pystr(),
                               location=LocationEnum.SPB,
                               published=True,
                               genre_id=created_genre.id,
                               image_url="https://google.com/")
        Logger.info("### Steps 2. Create movie")
        created_movie = api_service_super_admin_api.post_movie(movie)

        assert created_movie.genre.name == genre.name, (f"Wrong genre name. Actual: '{created_movie.genre.name}', "
                                                        f"but expected: '{genre.name}'")
