import logging
from web_pages.infinite_scroll_page import Page1
import pytest
import time
from config import config


class TestInfiniteScroll:
    URL = config.INFINITE_SCROLL_URL
    PARAGRAPH_COUNT = 0

    @pytest.mark.parametrize('aiming_paragraph_value', [19])
    def test_iframes(self, browser, aiming_paragraph_value):
        logger = logging.getLogger('logger')
        logger.info("Executing an infinite scroll test")
        browser.get(self.URL)

        self.page_1 = Page1(browser)
        self.page_1.wait_for_open()

        last_height = browser.execute_script("return document.body.scrollHeight")

        while True:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            paragraphs = self.page_1.find_all()
            self.PARAGRAPH_COUNT = len(paragraphs)
            logger.info(f"Current paragraph count: {self.PARAGRAPH_COUNT}")

            if self.PARAGRAPH_COUNT >= aiming_paragraph_value:
                break

            new_height = browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        assert self.PARAGRAPH_COUNT == aiming_paragraph_value,\
            f"Expected {aiming_paragraph_value} got instead {self.PARAGRAPH_COUNT}"
