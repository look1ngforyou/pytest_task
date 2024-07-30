import logging
from logging import StreamHandler, Formatter
import sys


def setup_logging():
    logger = logging.getLogger('logger')
    logger.setLevel(logging.INFO)
    handler = StreamHandler(stream=sys.stdout)
    handler.setFormatter(Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
    logger.addHandler(handler)
    return logger
