import pytest
import logging
from browser.browser import Browser
from logging_configuration.my_logger import setup_logging
from config import config


@pytest.fixture(scope='session', autouse=True)
def setup_logging_fixture():
    setup_logging()
    logger = logging.getLogger('logger')
    return logger


@pytest.fixture(scope='function')
def browser(setup_logging_fixture):
    browser = Browser(browser_type=config.BROWSER_TYPE, arguments=config.OPTIONS, headless=config.HEADLESS)
    yield browser
    browser.quit()
