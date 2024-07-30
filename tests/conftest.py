import pytest
import logging
from browser.browser import Browser
from logging_configuration.my_logger import setup_logging


@pytest.fixture(scope='session', autouse=True)
def setup_logging_fixture():
    setup_logging()
    logger = logging.getLogger('logger')
    logger.info("Logging setup complete")
    return logger


@pytest.fixture(scope='function')
def browser(setup_logging_fixture):
    logger = logging.getLogger('logger')
    browser = Browser("chrome")
    yield browser
    browser.quit()