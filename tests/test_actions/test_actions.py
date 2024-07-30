import logging
from web_pages.actions_page import Page1


class TestActions:
    URL = "https://the-internet.herokuapp.com/horizontal_slider"
    SLIDER_DIVISION_UNIT = 0.5
    slider_moving_value = 5
    slider_direction = "right"

    def test(self, browser):
        logger = logging.getLogger('logger')
        logger.info("Executing an action test")
        self.page_1 = Page1(browser)

        browser.get(self.URL)
        self.page_1.wait_for_open()

        self.page_1.move_slider(direction=self.slider_direction, value=self.slider_moving_value)

        expected_value = self.SLIDER_DIVISION_UNIT * self.slider_moving_value
        real_value = self.page_1.get_slider_value()

        assert real_value == expected_value, \
            f"The slider did not move to the specified value {expected_value}, moved instead to {real_value}"
