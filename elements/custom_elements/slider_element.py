from selenium.webdriver import Keys
from elements.base_element import BaseElement
import logging
from enum import Enum

logger = logging.getLogger('logger')


class Direction(str, Enum):
    RIGHT = "right"
    LEFT = "left"


class SliderElement(BaseElement):
    def move(self, direction: Direction, value):
        slider = self.get_presence_of_element_located()
        logger.info(f"{self.description} move slider to the {direction}")
        if direction == Direction.RIGHT:
            slider.send_keys(Keys.ARROW_RIGHT * value)
        elif direction == Direction.LEFT:
            slider.send_keys(Keys.ARROW_LEFT * value)
