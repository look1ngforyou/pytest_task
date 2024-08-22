import requests
from utilities.api_utilities import ApiUtilities


class GenreHelper:
    GENRES_ENDPOINT = "/genres"

    def __init__(self, api_utilities: ApiUtilities):
        self.api_utilities = api_utilities

    def get_genres(self) -> requests.Response:
        response = self.api_utilities.get(self.GENRES_ENDPOINT)
        return response

    def post_genre(self, json) -> requests.Response:
        response = self.api_utilities.post(self.GENRES_ENDPOINT, json=json)
        return response
