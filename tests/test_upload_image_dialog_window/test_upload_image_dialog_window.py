import logging
from web_pages.upload_image_dialog_window_page import Page1
from config import config
import pytest


class TestUploadImageViaFE:
    URL = config.UPLOAD_IMAGE_URL

    @pytest.mark.parametrize('image, image_name', [
        ("tests\\test_data\\test_photo.jpg", "test_photo.jpg")])
    def test_upload_image_via_fe(self, browser, image, image_name):
        logger = logging.getLogger('logger')
        logger.warning("Executing an upload image via file explorer test")
        browser.get(self.URL)

        self.page_1 = Page1(browser)
        self.page_1.wait_for_open()

        self.page_1.upload_image_via_fe(image)

        text = self.page_1.get_image_text()
        assert text == image_name, "The file name is not displaying"

        assert self.page_1.presence_of_check_mark_located(), "The check mark symbol has not appeared"
