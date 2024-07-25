import pytest
import logging
from browser.browser import Browser
from tests.test_upload_image.page1 import Page1
from logging_configuration.logger import setup_logging


@pytest.fixture
def browser():
    setup_logging()
    browser = Browser("chrome")

    yield browser
    browser.quit()


class TestUploadImage:
    URL = "http://the-internet.herokuapp.com/upload"
    IMAGE = "tests\\test_upload_image\\test_photo.jpg"
    IMAGE_NAME = "test_photo.jpg"

    def test(self, browser):
        logging.warning("Executing an upload image test")
        self.page_1 = Page1(browser)

        browser.get(self.URL)
        self.page_1.wait_for_open()

        self.page_1.input.send_keys(self.IMAGE)

        self.page_1.button.click()

        text = self.page_1.label.text()
        assert text == self.IMAGE_NAME, "The file name is not displaying"
        logging.warning("Successful interaction with an image upload")