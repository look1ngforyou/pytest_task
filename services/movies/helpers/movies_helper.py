import requests
from services.base_helper import BaseHelper
import json


class MovieHelper(BaseHelper):
    MOVIES_ENDPOINT = "movies/"
    GENRES_ENDPOINT = "genres/"

    def get_movies(self) -> requests.Response:
        response = self.api_utilities.get(self.MOVIES_ENDPOINT)
        return response

    def post_movie(self, json: json) -> requests.Response:
        response = self.api_utilities.post(self.MOVIES_ENDPOINT, json=json)
        return response
