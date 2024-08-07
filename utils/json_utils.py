import json


class JsonUtils:
    @staticmethod
    def is_json(obj: str) -> bool:
        """
        Check if text is json or not
        :param obj (str): string to be checked
        :return: obj is json or not
        :rtype: bool
        """
        try:
            json.loads(obj)
        except ValueError:
            return False
        return True