import pytest
import logging
from web_pages.hovers_page import Page1
from config import config


class TestHovers:
    URL = config.HOVERS_URL

    @pytest.mark.parametrize("index, username, link_piece", [
        (1, "name: user1", "/users/1"),
        (2, "name: user2", "/users/2"),
        (3, "name: user3", "/users/3"),
    ])
    def test_hovers(self, browser, index, username, link_piece):
        logger = logging.getLogger('logger')
        logger.info("Executing hover test")
        browser.get(self.URL)

        self.page_1 = Page1(browser)
        self.page_1.wait_for_open()

        self.page_1.hover_over_figure(index)
        text = self.page_1.get_caption_text(index)
        assert text == username, f"The required text {username} is not expected {text}"

        self.page_1.click_profile_label(index)
        current_url = browser.get_current_url()
        assert current_url.endswith(link_piece), f"Current url {current_url} is not opened for {link_piece}"


