from selenium.webdriver import Keys
from elements.base_element import BaseElement
import logging


class SliderElement(BaseElement):
    def __init__(self, driver, locator_1=None, attribute=None, timeout=15, direction=None, value=0):
        super().__init__(driver, locator_1 or (None, None), attribute, timeout)
        self.direction = direction
        self.value = value

    def move_the_slider_to_the_trajectory(self):
        slider = self.wait(self.driver, self.timeout).until(self.ec.presence_of_element_located(self.locator_1))
        logging.info(f"Moving slider {self.direction} with a locator: {self.locator_1}")
        if self.direction == "right":
            for _ in range(self.value):
                slider.send_keys(Keys.ARROW_RIGHT)
                logging.info("Moved slider to the right")
        elif self.direction == "left":
            for _ in range(self.value):
                slider.send_keys(Keys.ARROW_LEFT)
                logging.info("Moved slider to the left")