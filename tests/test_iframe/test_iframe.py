import logging
from web_pages.iframe_page import Page1
from config import config


class TestIframe:
    EXPECTED_PARENT_TEXT = "Parent frame"
    EXPECTED_CHILD_TEXT = "Child Iframe"

    def test_frames(self, browser):
        logger = logging.getLogger('logger')
        logger.info("Execute  iframe test")
        browser.get(config.IFRAME_URL)

        self.IframePage = Page1(browser)
        self.IframePage.wait_for_open()

        self.IframePage.redirection_to_iframes_page()

        assert self.IframePage.get_presence_of_title_located()

        parent_frame_element = self.IframePage.get_presence_of_parent_frame_located()
        browser.switch_to_iframe(parent_frame_element)

        actual_text = self.IframePage.get_frame_text()
        assert actual_text == self.EXPECTED_PARENT_TEXT, \
            f"Expected {self.EXPECTED_PARENT_TEXT} in iframe, got {actual_text} instead"

        child_frame_element = self.IframePage.get_presence_of_child_iframe_located()
        browser.switch_to_iframe(child_frame_element)

        actual_text = self.IframePage.get_iframe_text()
        assert actual_text == self.EXPECTED_CHILD_TEXT, \
            f"Expected {self.EXPECTED_CHILD_TEXT} in iframe, got {actual_text} instead"
