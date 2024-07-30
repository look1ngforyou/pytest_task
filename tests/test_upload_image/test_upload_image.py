import logging
from web_pages.upload_image_page import Page1


class TestUploadImage:
    URL = "https://the-internet.herokuapp.com/upload"
    IMAGE = "tests\\test_data\\test_photo.jpg"
    IMAGE_NAME = "test_photo.jpg"

    def test(self, browser):
        logger = logging.getLogger('logger')
        logger.warning("Executing an upload image test")
        self.page_1 = Page1(browser)

        browser.get(self.URL)
        self.page_1.wait_for_open()

        self.page_1.send_keys(self.IMAGE)

        self.page_1.click()

        text = self.page_1.text()
        assert text == self.IMAGE_NAME, "The file name is not displaying"
