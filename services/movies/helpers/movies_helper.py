from utils.api_utils import ApiUtils


class MoviesHelper:
    MOVIES_ENDPOINT = "/movies"

    def __init__(self, api_utils: ApiUtils):
        self.api_utils = api_utils

    def get_movies(self):
        response = self.api_utils.get(self.MOVIES_ENDPOINT)
        return response

    def post_movie(self, json):
        response = self.api_utils.post(self.MOVIES_ENDPOINT, json=json)
        return response
