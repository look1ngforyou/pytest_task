import requests
import json
from utilities.json_utilities import JsonUtils
from requests import Session
from logger.logger import Logger
import curlify


def log_response(function):
    def _log_response(*args, **kwargs) -> requests.Response:
        response = function(*args, **kwargs)
        Logger.info(f"Request curl: {curlify.to_curl(response.request)}")
        body = json.dumps(response.json(), indent=4) if JsonUtils.is_json(response.text) else response.text
        Logger.info(f"Response status code={response.status_code}, elapsed time = {response.elapsed}\n\n{body}\n")
        return response

    return _log_response


class ApiUtilities:
    def __init__(self, url, headers=None):
        if headers is None:
            headers = {}
        self.url = url
        self.session = Session()
        self.session.headers = headers

    @log_response
    def get(self, endpoint_url=None, **kwargs) -> requests.Response:
        response = self.session.get(self.url + endpoint_url, **kwargs)
        return response

    @log_response
    def post(self, endpoint_url, data=None, json=None, **kwargs) -> requests.Response:
        response = self.session.post(self.url + endpoint_url, data, json, **kwargs)
        return response

    @log_response
    def delete(self, endpoint_url, **kwargs) -> requests.Response:
        response = self.session.delete(self.url + endpoint_url, **kwargs)
        return response

    @log_response
    def patch(self, endpoint_url, **kwargs) -> requests.Response:
        response = self.session.patch(self.url + endpoint_url, **kwargs)
        return response

    def update_headers(self, headers: dict) -> None:
        self.session.headers.update(headers)
