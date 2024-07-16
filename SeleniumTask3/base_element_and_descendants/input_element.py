from base_element_and_descendants.base_element import BaseElement


class InputElement(BaseElement):
    def send_keys(self):
        self.driver.send_keys()
