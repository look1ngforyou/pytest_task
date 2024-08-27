import json


class JsonUtils:
    @staticmethod
    def is_json(file: str) -> bool:
        try:
            json.loads(file)
        except ValueError:
            return False
        return True
