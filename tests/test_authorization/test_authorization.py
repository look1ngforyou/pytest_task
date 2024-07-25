from browser.browser import Browser
from tests.test_authorization.page1 import Page1
import pytest
import logging
from logging_configuration.logger import setup_logging


@pytest.fixture
def browser():
    setup_logging()
    browser = Browser("chrome")

    yield browser
    browser.quit()


class TestAuthorization:
    BROWSER_TYPE = "chrome"
    login = "admin"
    password = "admin"
    URL = "https://{}:{}@the-internet.herokuapp.com/basic_auth".format(login, password)
    AUTHORIZATION_EXPECTED_TEXT = "Congratulations! You must have the proper credentials."

    def test(self, browser):
        logging.warning("Executing an authorization test")
        self.page_1 = Page1(browser)

        browser.get(self.URL)
        self.page_1.wait_for_open()

        actual_text = self.page_1.label_1.text()

        assert actual_text == self.AUTHORIZATION_EXPECTED_TEXT, \
            f"The required text {actual_text} is not expected {self.AUTHORIZATION_EXPECTED_TEXT}"
        logging.warning("Successful authorization!")
