from enum import Enum


class Status(str, Enum):
    SUCCESS = "SUCCESS"
    INVALID_CARD = "INVALID_CARD"
    ERROR = "ERROR"
