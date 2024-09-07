from selenium.webdriver.support.wait import WebDriverWait
from elements.base_element import BaseElement
import logging

logger = logging.getLogger('logger')


class InputElement(BaseElement):
    def send_keys(self, keys):
        logger.info(f" {self.description} sending keys {keys}")
        input_element = WebDriverWait(self.driver.get_driver, self.timeout).until(
            self.ec.visibility_of_element_located(self.locator))
        input_element.send_keys(keys)
