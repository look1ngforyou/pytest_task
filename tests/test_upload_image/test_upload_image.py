import logging
from web_pages.upload_image_page import Page1
from config import config
import pytest


class TestUploadImage:
    @pytest.mark.parametrize('image, expected_image_name', [
        ("tests\\test_data\\test_photo.jpg", "test_photo.jpg")])
    def test_upload_image(self, browser, image, expected_image_name):
        logger = logging.getLogger('logger')
        logger.info("Execute an upload image test")
        browser.get(config.UPLOAD_IMAGE_URL)

        self.UploadImagePage = Page1(browser)
        self.UploadImagePage.wait_for_open()

        self.UploadImagePage.upload_image(image)

        actual_name = self.UploadImagePage.get_image_text()
        assert actual_name == expected_image_name, "The file name is not displaying"
