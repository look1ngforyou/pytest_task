import pytest
import logging
from tests.test_actions.page1 import Page1
from browser.browser import Browser
from logging_configuration.logger import setup_logging


@pytest.fixture
def browser():
    setup_logging()
    browser = Browser("chrome")

    yield browser
    browser.quit()


class TestActions:
    URL = "https://the-internet.herokuapp.com/horizontal_slider"
    UNIT = 0.5

    def test(self, browser):
        logging.warning("Executing an action test")
        self.page_1 = Page1(browser)

        browser.get(self.URL)
        self.page_1.wait_for_open()

        self.page_1.slider.move_the_slider_to_the_trajectory()

        real_value = float(self.page_1.label.text())
        expected_value = self.UNIT * self.page_1.VALUE
        assert real_value == expected_value,\
            f"The slider did not move to the specified value {expected_value}, moved instead to {real_value}"
        logging.warning("Successful interaction with an action")
