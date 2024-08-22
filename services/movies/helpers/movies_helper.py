import requests
from utilities.api_utilities import ApiUtilities


class MovieHelper:
    MOVIES_ENDPOINT = "/movies/"
    GENRES_ENDPOINT = "/genres"

    def __init__(self, api_utilities: ApiUtilities):
        self.api_utilities = api_utilities

    def get_movies(self) -> requests.Response:
        response = self.api_utilities.get(self.MOVIES_ENDPOINT)
        return response

    def post_movie(self, json) -> requests.Response:
        response = self.api_utilities.post(self.MOVIES_ENDPOINT, json=json)
        return response


