import pytest
import logging
from tests.test_infinite_scroll.page1 import Page1
from browser.browser import Browser
from logging_configuration.logger import setup_logging


@pytest.fixture
def browser():
    setup_logging()
    browser = Browser("chrome")

    yield browser
    browser.quit()


class TestInfiniteScroll:
    URL = "https://the-internet.herokuapp.com/infinite_scroll"
    AIMING_PARAGRAPH_VALUE = 19

    def test(self, browser):
        logging.warning("Executing an infinite scroll test")
        self.page_1 = Page1(browser)

        browser.get(self.URL)
        self.page_1.wait_for_open()

        while self.page_1.get_paragraph_count() < self.AIMING_PARAGRAPH_VALUE:
            self.page_1.scroll_down()
            logging.info(f"Current paragraph count: {self.page_1.get_paragraph_count()}")

        assert self.page_1.get_paragraph_count() >= self.AIMING_PARAGRAPH_VALUE,\
            f"The paragraphs amount {self.AIMING_PARAGRAPH_VALUE} is not matching"
        logging.warning("Successful interaction with an infinite scroll")


