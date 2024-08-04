import logging

logger = logging.getLogger('logger')


class BasePage:
    UNIQUE_ELEMENT_LOC = None

    def __init__(self, driver, unique_element):
        self.driver = driver
        self.unique_element = unique_element

    def wait_for_open(self) -> None:
        logger.info("Wait for unique element to open")
        self.unique_element.get_presence_of_element_located()
