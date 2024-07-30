from selenium.webdriver import Keys
from elements.base_element import BaseElement
import logging


class SliderElement(BaseElement):
    RIGHT = "right"
    LEFT = "left"

    def __init__(self, driver, locator_1=None, timeout=15, description=None):
        super().__init__(driver, locator_1 or (None, None), timeout, description)

    def move_the_slider_to_the_trajectory(self, direction, value):
        slider = self.wait(self.driver, self.timeout).until(self.ec.presence_of_element_located(self.locator_1))
        logging.info(f"{self.description} moving slider to the {direction}")
        if direction == self.RIGHT:
            for _ in range(value):
                slider.send_keys(Keys.ARROW_RIGHT)
        elif direction == self.LEFT:
            for _ in range(value):
                slider.send_keys(Keys.ARROW_LEFT)
