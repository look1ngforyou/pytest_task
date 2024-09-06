import pytest
import logging
from web_pages.hovers_page import Page1
from config import config


class TestHovers:
    @pytest.mark.parametrize("index, username, link_piece", [
        (1, "name: user1", "/users/1"),
        (2, "name: user2", "/users/2"),
        (3, "name: user3", "/users/3"),
    ])
    def test_hovers(self, browser, index, username, link_piece):
        logger = logging.getLogger('logger')
        logger.info("Execute hover test")
        browser.get(config.HOVERS_URL)

        self.hovers_page = Page1(browser)
        self.hovers_page.wait_for_open()

        self.hovers_page.hover_over_figure(index)
        actual_text = self.hovers_page.get_caption_text(index)
        assert actual_text == username, f"The required text {username} is not expected {actual_text}"

        self.hovers_page.click_profile_label(index)
        current_url = browser.get_current_url()
        assert current_url.endswith(link_piece), f"Current url {current_url} is not opened for {link_piece}"
