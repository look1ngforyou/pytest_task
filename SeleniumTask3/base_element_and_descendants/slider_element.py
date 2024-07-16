from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base_element_and_descendants.base_element import BaseElement
import logging


class SliderElement(BaseElement):
    def move_slider(self, locator, offset, timeout=10):
        logging.info(
            f"Waiting for slider by locator: {locator} offset: {offset} and timeout: {timeout}to be present to move it")
        element = WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))
        logging.info(f"Slider is present, trying to move it")
        action_chains = ActionChains(self.driver)
        action_chains.click_and_hold(element).move_by_offset(offset, 0).release().perform()
        logging.info(f"Successfully moved slider")

    def get_slider_value(self, locator, timeout=10):
        logging.info(
            f"Waiting for slider value by locator: {locator} and timeout: {timeout} to be present to get it value")
        element = WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))
        logging.info(f"Slider value is present, with value: {element}")
        return float(element.get_attribute("value"))
