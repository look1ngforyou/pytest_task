from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
import logging

logging.basicConfig(
    filename='test.log',
    level=logging.INFO,
    filemode="w",
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


class BaseElement:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def click_on_element(self, locator, timeout=15):
        self.logger.info(
            f"Waiting for element with locator: {locator} and timeout: {timeout} to be clickable to click on it")
        element = WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator))
        self.logger.info("Element is clickable, trying to click")
        element.click()
        self.logger.info("Successfully clicked on element")

    def get_text(self, locator, timeout=15):
        self.logger.info(
            f"Waiting for element with locator: {locator} and timeout: {timeout} to be present and get text")
        element = WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))
        self.logger.info("Element is present, trying to get text")
        self.logger.info(f"Returning text: {element.text}")
        return element.text

    def presence_located(self, locator, timeout=15):
        self.logger.info(f"Waiting for element with locator: {locator} and timeout: {timeout} to be present")
        element = WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))
        self.logger.info("Element is present")
        return element

    def presence_of_elements_located(self, locator, timeout=15):
        self.logger.info(f"Waiting for elements with locator: {locator} and timeout: {timeout} to be present")
        elements = WebDriverWait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))
        return elements

    def visibility_located(self, locator, timeout=15):
        self.logger.info(f"Waiting for element with locator: {locator} and timeout: {timeout} to be visible")
        element = WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
        self.logger.info("Element is visible")
        return element

    def get_attribute(self, locator, attribute, timeout=15):
        self.logger.info(f"Getting attribute '{attribute}' from element with locator: {locator} and timeout: {timeout}")
        element = WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))
        value = element.get_attribute(attribute)
        self.logger.info(f"Successfully retrieved attribute '{attribute}': {value}")
        return value

    def right_click(self, locator, timeout=15):
        self.logger.info(
            f"Waiting for element with locator: {locator} and timeout: {timeout} to be present to right click")
        element = WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))
        self.logger.info("Element is present")
        self.logger.info("Trying to right click")
        action_chains = ActionChains(self.driver)
        action_chains.context_click(element).perform()
        self.logger.info("Successfully right clicked")

    def hover_over_element(self, locator, timeout=15):
        self.logger.info(
            f"Waiting for element with locator: {locator} and timeout: {timeout} to be visible to hover over")
        element = WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
        self.logger.info("Element is visible")
        self.logger.info("Trying to hover over element")
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(element).perform()
        self.logger.info("Successfully hovered over element")
