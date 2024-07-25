import pytest
import logging
from tests.test_hovers.page1 import Page1
from browser.browser import Browser
from logging_configuration.logger import setup_logging


@pytest.fixture
def browser():
    setup_logging()
    browser = Browser("chrome")

    yield browser
    browser.quit()


class TestHovers:
    URL = "https://the-internet.herokuapp.com/hovers"
    USERNAMES = ["name: user1", "name: user2", "name: user3"]
    LINK_PIECES = ["/users/1", "/users/2", "/users/3"]

    @pytest.mark.parametrize("index, username, link_piece", [
        (1, "name: user1", "/users/1"),
        (2, "name: user2", "/users/2"),
        (3, "name: user3", "/users/3"),
    ])
    def test_hover(self, browser, index, username, link_piece):
        logging.warning("Executing hover test")
        self.page_1 = Page1(browser)

        browser.get(self.URL)
        self.page_1.wait_for_open()

        self.page_1.get_figure(index).hover_over_element()
        text = self.page_1.get_caption(index).text()
        assert text == username, f"The required text {username} is not expected {text}"

        self.page_1.get_profile_label(index).click()
        current_url = browser.current_url()
        assert current_url.endswith(link_piece), f"Current url {current_url} is not opened for {link_piece}"
        logging.warning("Executed hover interaction")


