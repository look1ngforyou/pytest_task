import logging
from web_pages.infinite_scroll_page import Page1
import time


class TestInfiniteScroll:
    URL = "https://the-internet.herokuapp.com/infinite_scroll"
    AIMING_PARAGRAPH_VALUE = 12
    PARAGRAPH_COUNT = 0

    def test(self, browser):
        logger = logging.getLogger('logger')
        logger.info("Executing an infinite scroll test")
        self.page_1 = Page1(browser)

        browser.get(self.URL)
        self.page_1.wait_for_open()

        last_height = browser.execute_script("return document.body.scrollHeight")

        while self.PARAGRAPH_COUNT < self.AIMING_PARAGRAPH_VALUE:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            time.sleep(1)

            paragraphs = self.page_1.find_all()
            paragraph_count = len(paragraphs)

            new_height = browser.execute_script("return document.body.scrollHeight")
            logger.info(f"Current paragraph count: {paragraph_count}")
            if new_height == last_height:
                break
            last_height = new_height

        assert self.PARAGRAPH_COUNT == self.AIMING_PARAGRAPH_VALUE,\
            f"Expected {self.AIMING_PARAGRAPH_VALUE} got instead {self.PARAGRAPH_COUNT}"
