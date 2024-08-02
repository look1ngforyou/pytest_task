import logging
from web_pages.infinite_scroll_page import Page1
import pytest
from config import config


class TestInfiniteScroll:

    @pytest.mark.parametrize('aiming_paragraph_value', [5])
    def test_infinite_scroll(self, browser, aiming_paragraph_value):
        logger = logging.getLogger('logger')
        logger.info("Execute an infinite scroll test")
        browser.get(config.INFINITE_SCROLL_URL)

        self.InfScrollPage = Page1(browser)
        self.InfScrollPage.wait_for_open()

        actual_paragraphs_count = self.InfScrollPage.scroll_through_paragraphs_to_aimed_value(aiming_paragraph_value)

        assert actual_paragraphs_count == aiming_paragraph_value,\
            f"Expected {aiming_paragraph_value} got instead {actual_paragraphs_count}"
