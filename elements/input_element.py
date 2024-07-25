from elements.base_element import BaseElement
import logging


class InputElement(BaseElement):
    def send_keys(self, keys):
        logging.info(f"Sending keys to an element with a locator {self.locator_1}")
        input_element = self.wait(self.driver, self.timeout).until(self.ec.presence_of_element_located(self.locator_1))
        input_element.send_keys(keys)
        logging.info(f"Sent keys {keys}")
