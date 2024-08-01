from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from elements.base_element import BaseElement
from constants.direction import Direction
import logging

logger = logging.getLogger('logger')


class SliderElement(BaseElement):

    def __init__(self, driver, locator_1, timeout=15, description=None):
        super().__init__(driver, locator_1, timeout, description)

    def move(self, direction: Direction, value):
        slider = WebDriverWait(self.driver._get_driver(), self.timeout).until(self.ec.presence_of_element_located(self.locator_1))
        logger.info(f"{self.description} moving slider to the {direction}")
        if direction == Direction.RIGHT:
            for _ in range(value):
                slider.send_keys(Keys.ARROW_RIGHT)
        elif direction == Direction.LEFT:
            for _ in range(value):
                slider.send_keys(Keys.ARROW_LEFT)

