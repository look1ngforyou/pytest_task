from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import logging

logger = logging.getLogger('logger')


class BaseElement:
    DEFAULT_TIMEOUT = 15

    def __init__(self, driver, locator_1, timeout: int = DEFAULT_TIMEOUT, description: str = None):
        self.driver = driver
        self.locator_1 = locator_1
        self.timeout = timeout
        self.ec = ec
        self.description = description

    def presence_of_element_located(self):
        logger.info(f"{self.description} finding presence of the element")
        element = WebDriverWait(self.driver._get_driver(), self.timeout).until(
            self.ec.presence_of_element_located(self.locator_1))
        return element

    def presence_of_elements_located(self):
        logger.info(f"{self.description} finding presence of the elements")
        elements = WebDriverWait(self.driver._get_driver(), self.timeout).until(
            self.ec.presence_of_all_elements_located(self.locator_1))
        logger.info(f"Found presence of the elements: {elements}")
        return elements

    def text(self):
        logger.info(f"{self.description} getting an element text")
        element = self.presence_of_element_located()
        text = element.text
        logger.info(f"Received an element text: {text}")
        return text

    def visibility_located(self):
        logger.info(f"Finding visibility of an element with a locator: {self.locator_1}")
        element = WebDriverWait(self.driver._get_driver(), self.timeout).until(
            self.ec.visibility_of_element_located(self.locator_1))
        logger.info("Element is visible")
        return element

    def get_attribute(self, attribute):
        logger.info(f"{self.description} getting attribute '{attribute}' from an element")
        element = self.presence_of_element_located()
        value = element.get_attribute(attribute)
        logger.info(f"Retrieved attribute {value}")
        return value

    def click(self):
        logger.info(f"{self.description} clicking on an element")
        element = WebDriverWait(self.driver._get_driver(), self.timeout).until(
            self.ec.element_to_be_clickable(self.locator_1))
        element.click()

    def right_click(self):
        logger.info(f"{self.description} right clicking on an element")
        element = WebDriverWait(self.driver._get_driver(), self.timeout).until(
            self.ec.element_to_be_clickable(self.locator_1))
        action_chains = ActionChains(self.driver._get_driver())
        action_chains.context_click(element).perform()

    def hover_over_element(self):
        logger.info(f"{self.description} hovering on an element")
        element = self.visibility_located()
        action_chains = ActionChains(self.driver._get_driver())
        action_chains.move_to_element(element).perform()

    def scroll_into_view(self):
        logger.info(f"{self.description} scrolling to the element")
        element = self.presence_of_element_located()
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_down(self):
        logger.info("Scrolling down")
        element = self.presence_of_element_located()
        element.send_keys(Keys.PAGE_DOWN)
