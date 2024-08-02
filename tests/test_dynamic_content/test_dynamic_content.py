import logging
from web_pages.dynamic_content_page import Page1
from config import config


class TestDynamicContent:
    def test_dynamic_content(self, browser):
        logger = logging.getLogger('logger')
        logger.info("Execute a dynamic content test")
        browser.get(config.DYNAMIC_CONTENT_URL)

        self.DynamicContentPage = Page1(browser)
        self.DynamicContentPage.wait_for_open()

        images_sources = self.DynamicContentPage.get_images_sources()

        while len(set(images_sources)) == 3:
            browser.refresh()
            images_sources = self.DynamicContentPage.get_images_sources()

        image_1 = images_sources[0]
        image_2 = images_sources[1]
        image_3 = images_sources[2]

        assert image_1 == image_2 or image_1 == image_3 or image_2 == image_3, "The images do not match"
