from web_pages.authorization_page import Page1
import logging
from config import config


class TestAuthorization:
    LOGIN = "admin"
    PASS = "admin"
    URL = config.AUTHORIZATION_URL.format(LOGIN, PASS)
    AUTHORIZATION_EXPECTED_TEXT = "Congratulations! You must have the proper credentials."

    def test_authorization(self, browser):
        logger = logging.getLogger('logger')
        logger.info("Executing an authorization test")
        browser.get(self.URL)

        self.page_1 = Page1(browser)
        self.page_1.wait_for_open()

        page_text = self.page_1.page_text()

        assert page_text == self.AUTHORIZATION_EXPECTED_TEXT, \
            f"The required text {page_text} is not expected {self.AUTHORIZATION_EXPECTED_TEXT}"
