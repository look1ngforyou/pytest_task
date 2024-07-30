import logging
from web_pages.dynamic_content_page import Page1


class TestDynamicContent:
    URL = "https://the-internet.herokuapp.com/dynamic_content"

    def test(self, browser):
        logger = logging.getLogger('logger')
        logger.info("Executing an dynamic content test")
        self.page_1 = Page1(browser)

        browser.get(self.URL)
        self.page_1.wait_for_open()

        image_1 = self.page_1.image_1_attribute()
        image_2 = self.page_1.image_2_attribute()
        image_3 = self.page_1.image_3_attribute()

        while len({image_1, image_2, image_3}) == 3:
            browser.refresh()
            image_1 = self.page_1.image_1_attribute()
            image_2 = self.page_1.image_2_attribute()
            image_3 = self.page_1.image_3_attribute()

        assert image_1 == image_2 or image_1 == image_3 or image_2 == image_3, "The images do not match"
