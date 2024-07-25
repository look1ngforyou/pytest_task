import pytest
import logging
from browser.browser import Browser
from tests.test_upload_image_dialog_window.page1 import Page1
from test_utils.test_utils import upload_file_via_fe
from logging_configuration.logger import setup_logging


@pytest.fixture
def browser():
    setup_logging()
    browser = Browser("chrome")

    yield browser
    browser.quit()


class TestUploadImageViaFE:
    URL = "https://the-internet.herokuapp.com/upload"
    IMAGE = "tests\\test_upload_image\\test_photo.jpg"
    IMAGE_NAME = "test_photo.jpg"

    def test(self, browser):
        logging.warning("Executing an upload image via file explorer test")
        self.page_1 = Page1(browser)

        browser.get(self.URL)
        self.page_1.wait_for_open()

        self.page_1.web_element_1.click()

        upload_file_via_fe(self.IMAGE)

        text = self.page_1.label.text()
        assert text == self.IMAGE_NAME, "The file name is not displaying"

        assert self.page_1.web_element_2.presence_of_element_located(), "The confirm symbol has not appeared"
        logging.warning("Successful interaction with an image upload vif file explorer")