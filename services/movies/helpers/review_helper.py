import requests
from services.base_helper import BaseHelper


class ReviewHelper(BaseHelper):
    MOVIES_ENDPOINT = "movies/"
    REVIEWS_ENDPOINT = "/reviews/"
    SHOW_REVIEW_ENDPOINT = "show/"

    def post_movie_review(self, movie_id: int, json) -> requests.Response:
        response = self.api_utilities.post(self.MOVIES_ENDPOINT + str(movie_id) + self.REVIEWS_ENDPOINT, json=json)
        return response

    def patch_movie_review(self, movie_id: int, user_id: str) -> requests.Response:
        response = self.api_utilities.patch(
            self.MOVIES_ENDPOINT + str(movie_id) + self.REVIEWS_ENDPOINT + self.SHOW_REVIEW_ENDPOINT + user_id)
        return response

    def delete_review(self, movie_id: int) -> requests.Response:
        response = self.api_utilities.delete(self.MOVIES_ENDPOINT + str(movie_id) + self.REVIEWS_ENDPOINT)
        return response
