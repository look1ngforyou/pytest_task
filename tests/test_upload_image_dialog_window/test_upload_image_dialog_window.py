import logging
from web_pages.upload_image_dialog_window_page import Page1
from test_utils.test_utils import upload_file_via_fe


class TestUploadImageViaFE:
    URL = "https://the-internet.herokuapp.com/upload"
    IMAGE = "tests\\test_data\\test_photo.jpg"
    IMAGE_NAME = "test_photo.jpg"

    def test(self, browser):
        logger = logging.getLogger('logger')
        logger.warning("Executing an upload image via file explorer test")
        self.page_1 = Page1(browser)

        browser.get(self.URL)
        self.page_1.wait_for_open()

        self.page_1.click()

        upload_file_via_fe(self.IMAGE)

        text = self.page_1.text()
        assert text == self.IMAGE_NAME, "The file name is not displaying"

        assert self.page_1.presence_of_check_mark_located(), "The check mark symbol has not appeared"
