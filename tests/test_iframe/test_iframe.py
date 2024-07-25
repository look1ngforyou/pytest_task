import pytest
import logging
from tests.test_iframe.page1 import Page1
from browser.browser import Browser
from logging_configuration.logger import setup_logging


@pytest.fixture
def browser():
    setup_logging()
    browser = Browser("chrome")

    yield browser
    browser.quit()


class Test:
    URL = "https://demoqa.com/alertsWindows"
    PARENT_TEXT = "Parent frame"
    CHILD_TEXT = "Child Iframe"

    def test_frames(self, browser):
        logging.warning("Executing iframe test")
        self.page_1 = Page1(browser)

        browser.get(self.URL)
        self.page_1.wait_for_open()

        self.page_1.label.scroll_to_element()
        self.page_1.label.click()

        assert self.page_1.title.presence_of_element_located()

        parent_frame_element = self.page_1.parent_frame.presence_of_element_located()
        browser.switch_to_iframe(parent_frame_element)

        text = self.page_1.label_frame.text()
        assert text == self.PARENT_TEXT, f"Expected {self.PARENT_TEXT} in iframe, got {text} instead"

        child_frame_element = self.page_1.child_iframe.presence_of_element_located()
        browser.switch_to_iframe(child_frame_element)

        text = self.page_1.label_iframe.text()
        assert text == self.CHILD_TEXT, f"Expected {self.PARENT_TEXT} in iframe, got {text} instead"
        logging.warning("Successful interaction with an iframes")