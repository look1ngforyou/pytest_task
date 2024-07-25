import logging


class BasePage:
    UNIQUE_ELEMENT_LOC = None

    def __init__(self, driver, unique_element):
        self.driver = driver
        self.unique_element = unique_element

    def wait_for_open(self) -> None:
        logging.info("Waiting for  unique element to open")
        self.unique_element.presence_of_element_located()
        logging.info("Unique element has opened")
