from web_pages.authorization_page import Page1
import logging


class TestAuthorization:
    login = "admin"
    password = "admin"
    URL = "https://{}:{}@the-internet.herokuapp.com/basic_auth".format(login, password)
    AUTHORIZATION_EXPECTED_TEXT = "Congratulations! You must have the proper credentials."

    def test(self, browser):
        logger = logging.getLogger('logger')
        logger.info("Executing an authorization test")
        self.page_1 = Page1(browser)

        browser.get(self.URL)
        self.page_1.wait_for_open()

        actual_text = self.page_1.text()

        assert actual_text == self.AUTHORIZATION_EXPECTED_TEXT, \
            f"The required text {actual_text} is not expected {self.AUTHORIZATION_EXPECTED_TEXT}"
