import logging
from web_pages.actions_page import Page1
import pytest
from config import config


class TestActions:
    URL = config.ACTIONS_URL
    SLIDER_DIVISION_UNIT = 0.5

    @pytest.mark.parametrize("slider_moving_value, slider_direction",
                             [(5, "right")])
    def test(self, browser, slider_moving_value, slider_direction):
        logger = logging.getLogger('logger')
        logger.info("Executing an action test")
        browser.get(self.URL)

        self.page_1 = Page1(browser)
        self.page_1.wait_for_open()

        self.page_1.move_slider(direction=slider_direction, value=slider_moving_value)

        expected_value = self.SLIDER_DIVISION_UNIT * slider_moving_value
        real_value = self.page_1.get_slider_value()

        assert real_value == expected_value, \
            f"The slider did not move to the specified value {expected_value}, moved instead to {real_value}"
