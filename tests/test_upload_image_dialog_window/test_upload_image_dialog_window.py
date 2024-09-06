import logging
from web_pages.upload_image_dialog_window_page import Page1
from config import config
import pytest

skip_condition = True


class TestUploadImageViaFE:
    @pytest.mark.skipif(skip_condition, reason="Skipping this test for demonstration purposes")
    @pytest.mark.parametrize('image, expected_image_name', [
        ("tests\\test_data\\test_photo.jpg", "test_photo.jpg")])
    def test_upload_image_via_fe(self, browser, image, expected_image_name):
        logger = logging.getLogger('logger')
        logger.info("Execute an upload image via file explorer test")
        browser.get(config.UPLOAD_IMAGE_URL)

        self.upload_image_page = Page1(browser)
        self.upload_image_page.wait_for_open()

        self.upload_image_page.upload_image_via_fe(image)

        actual_name = self.upload_image_page.get_image_text()
        assert actual_name == expected_image_name, "The file name is not displaying"

        assert self.upload_image_page.presence_of_check_mark_located(), "The check mark symbol has not appeared"
