import pytest
import logging
from tests.test_dynamic_content.page1 import Page1
from browser.browser import Browser
from logging_configuration.logger import setup_logging


@pytest.fixture
def browser():
    setup_logging()
    browser = Browser("chrome")

    yield browser
    browser.quit()


class TestDynamicContent:
    URL = "https://the-internet.herokuapp.com/dynamic_content"

    def test(self, browser):
        logging.warning("Executing an dynamic content test")
        self.page_1 = Page1(browser)

        browser.get(self.URL)
        self.page_1.wait_for_open()

        image_1 = self.page_1.image_1.get_attribute()
        image_2 = self.page_1.image_2.get_attribute()
        image_3 = self.page_1.image_3.get_attribute()

        while len({image_1, image_2, image_3}) == 3:
            browser.refresh()
            image_1 = self.page_1.image_1.get_attribute()
            image_2 = self.page_1.image_2.get_attribute()
            image_3 = self.page_1.image_3.get_attribute()

        assert image_1 == image_2 or image_1 == image_3 or image_2 == image_3, "The images do not match"
        logging.warning("Successful interaction with a dynamic content")