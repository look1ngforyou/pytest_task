import logging
from web_pages.iframe_page import Page1


class Test:
    URL = "https://demoqa.com/alertsWindows"
    PARENT_TEXT = "Parent frame"
    CHILD_TEXT = "Child Iframe"

    def test_frames(self, browser):
        logger = logging.getLogger('logger')
        logger.info("Executing iframe test")
        self.page_1 = Page1(browser)

        browser.get(self.URL)
        self.page_1.wait_for_open()

        self.page_1.scroll_into_view()
        self.page_1.click()

        assert self.page_1.presence_of_title_located()

        parent_frame_element = self.page_1.presence_of_parent_frame_located()
        browser.switch_to_iframe(parent_frame_element)

        text = self.page_1.frame_text()
        assert text == self.PARENT_TEXT, f"Expected {self.PARENT_TEXT} in iframe, got {text} instead"

        child_frame_element = self.page_1.presence_of_child_iframe_located()
        browser.switch_to_iframe(child_frame_element)

        text = self.page_1.iframe_text()
        assert text == self.CHILD_TEXT, f"Expected {self.PARENT_TEXT} in iframe, got {text} instead"
