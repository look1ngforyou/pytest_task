from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import logging

logger = logging.getLogger('logger')


class BaseElement:
    DEFAULT_TIMEOUT = 15

    def __init__(self, driver, locator, timeout: int = DEFAULT_TIMEOUT, description: str = None):
        self.driver = driver
        self.locator = locator
        self.timeout = timeout
        self.ec = ec
        self.description = description

    def presence_of_element_located(self):
        logger.info(f"{self.description} find presence of the element")
        element = WebDriverWait(self.driver.get_driver, self.timeout).until(
            self.ec.presence_of_element_located(self.locator))
        return element

    @property
    def text(self):
        logger.info(f"{self.description} get an element text")
        element = self.presence_of_element_located()
        text = element.text
        logger.info(f"Received an element text: {text}")
        return text

    def visibility_located(self):
        logger.info(f"Find visibility of an element with a locator: {self.locator}")
        element = WebDriverWait(self.driver.get_driver, self.timeout).until(
            self.ec.visibility_of_element_located(self.locator))
        logger.info("Element is visible")
        return element

    def get_attribute(self, attribute):
        logger.info(f"{self.description} get attribute '{attribute}' from an element")
        element = self.presence_of_element_located()
        value = element.get_attribute(attribute)
        logger.info(f"Retrieved attribute {value}")
        return value

    def click(self):
        logger.info(f"{self.description} click")
        element = WebDriverWait(self.driver.get_driver, self.timeout).until(
            self.ec.element_to_be_clickable(self.locator))
        element.click()

    def right_click(self):
        logger.info(f"{self.description} right click")
        element = WebDriverWait(self.driver.get_driver, self.timeout).until(
            self.ec.element_to_be_clickable(self.locator))
        action_chains = ActionChains(self.driver.get_driver)
        action_chains.context_click(element).perform()

    def hover_over_element(self):
        logger.info(f"{self.description} hover on an element")
        element = self.visibility_located()
        action_chains = ActionChains(self.driver.get_driver)
        action_chains.move_to_element(element).perform()

    def scroll_into_view(self):
        logger.info(f"{self.description} scroll to the element")
        element = self.presence_of_element_located()
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
