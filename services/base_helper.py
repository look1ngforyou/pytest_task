from utilities.api_utilities import ApiUtilities


class BaseHelper:
    def __init__(self, api_utilities: ApiUtilities):
        self.api_utilities = api_utilities
