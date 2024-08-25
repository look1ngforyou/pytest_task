import requests
from services.base_helper import BaseHelper
import json


class GenreHelper(BaseHelper):
    GENRES_ENDPOINT = "genres/"

    def get_genres(self) -> requests.Response:
        response = self.api_utilities.get(self.GENRES_ENDPOINT)
        return response

    def post_genre(self, json: json) -> requests.Response:
        response = self.api_utilities.post(self.GENRES_ENDPOINT, json=json)
        return response
