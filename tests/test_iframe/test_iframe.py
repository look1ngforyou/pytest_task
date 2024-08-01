import logging
from web_pages.iframe_page import Page1
from config import config


class TestIframe:
    URL = config.IFRAME_URL
    PARENT_TEXT = "Parent frame"
    CHILD_TEXT = "Child Iframe"

    def test_frames(self, browser):
        logger = logging.getLogger('logger')
        logger.info("Executing iframe test")
        browser.get(self.URL)

        self.page_1 = Page1(browser)
        self.page_1.wait_for_open()

        self.page_1.redirection_to_iframes_page()

        assert self.page_1.presence_of_title_located()

        parent_frame_element = self.page_1.presence_of_parent_frame_located()
        browser.switch_to_iframe(parent_frame_element)

        text = self.page_1.get_frame_text()
        assert text == self.PARENT_TEXT, f"Expected {self.PARENT_TEXT} in iframe, got {text} instead"

        child_frame_element = self.page_1.presence_of_child_iframe_located()
        browser.switch_to_iframe(child_frame_element)

        text = self.page_1.get_iframe_text()
        assert text == self.CHILD_TEXT, f"Expected {self.PARENT_TEXT} in iframe, got {text} instead"
