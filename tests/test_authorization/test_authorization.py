from web_pages.authorization_page import Page1
import logging
from config import config


class TestAuthorization:
    LOGIN = "admin"
    PASS = "admin"
    AUTHORIZATION_EXPECTED_TEXT = "Congratulations! You must have the proper credentials."

    def test_authorization(self, browser):
        logger = logging.getLogger('logger')
        logger.info("Execute an authorization test")
        browser.get(config.AUTHORIZATION_URL.format(self.LOGIN, self.PASS))

        self.AuthorizationPage = Page1(browser)
        self.AuthorizationPage.wait_for_open()

        actual_page_text = self.AuthorizationPage.get_page_text()

        assert actual_page_text == self.AUTHORIZATION_EXPECTED_TEXT, \
            f"The required text {actual_page_text} is not expected {self.AUTHORIZATION_EXPECTED_TEXT}"
