import requests
from utilities.api_utilities import ApiUtilities


class ReviewHelper:
    MOVIES_ENDPOINT = "/movies/"
    REVIEWS_ENDPOINT = "/reviews/"
    SHOW_REVIEW_ENDPOINT = "show/"

    def __init__(self, api_utilities: ApiUtilities):
        self.api_utilities = api_utilities

    def post_movie_review(self, movie_id, json) -> requests.Response:
        response = self.api_utilities.post(self.MOVIES_ENDPOINT + str(movie_id) + self.REVIEWS_ENDPOINT, json=json)
        return response

    def patch_movie_review(self, movie_id, user_id) -> requests.Response:
        response = self.api_utilities.patch(
            self.MOVIES_ENDPOINT + str(movie_id) + self.REVIEWS_ENDPOINT + self.SHOW_REVIEW_ENDPOINT + user_id)
        return response

    def delete_review(self, movie_id) -> requests.Response:
        response = self.api_utilities.delete(self.MOVIES_ENDPOINT + str(movie_id) + self.REVIEWS_ENDPOINT)
        return response
