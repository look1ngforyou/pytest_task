import logging
from web_pages.actions_page import Page1
import pytest
from config import config


class TestActions:
    SLIDER_DIVISION_UNIT = 0.5

    @pytest.mark.parametrize("slider_moving_value, slider_direction",
                             [(8, "right")])
    def test_actions(self, browser, slider_moving_value, slider_direction):
        logger = logging.getLogger('logger')
        logger.info("Execute an action test")
        browser.get(config.ACTIONS_URL)

        self.actions_page = Page1(browser)
        self.actions_page.wait_for_open()

        self.actions_page.move_slider(direction=slider_direction, value=slider_moving_value)

        expected_result = self.SLIDER_DIVISION_UNIT * slider_moving_value
        actual_result = self.actions_page.get_slider_value()

        assert actual_result == expected_result, \
            f"The slider did not move to the specified value {expected_result}, moved instead to {actual_result}"
