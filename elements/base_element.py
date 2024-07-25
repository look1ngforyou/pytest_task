from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import logging


class BaseElement:
    DEFAULT_TIMEOUT = 15

    def __init__(self, driver, locator_1, attribute=None, timeout: int = DEFAULT_TIMEOUT):
        self.driver = driver
        self.locator_1 = locator_1
        self.attribute = attribute
        self.timeout = timeout
        self.wait = WebDriverWait
        self.ec = ec

    def click(self):
        logging.info(f"Clicking on an element with a locator: {self.locator_1}")
        element = self.wait(self.driver, self.timeout).until(self.ec.element_to_be_clickable(self.locator_1))
        element.click()
        logging.info("Clicked on an element")

    def text(self):
        logging.info(f"Getting an element text with a locator: {self.locator_1}")
        element = self.wait(self.driver, self.timeout).until(self.ec.visibility_of_element_located(self.locator_1))
        text = element.text
        logging.info(f"Received an element text: {text}")
        return text

    def presence_of_element_located(self):
        logging.info(f"Finding presence of the element with a locator: {self.locator_1}")
        element = self.wait(self.driver, self.timeout).until(self.ec.presence_of_element_located(self.locator_1))
        logging.info(f"Found presence of the element: {element} ")
        return element

    def presence_of_elements_located(self):
        logging.info(f"Finding presence of the elements with a locator: {self.locator_1}")
        elements = self.wait(self.driver, self.timeout).until(self.ec.presence_of_all_elements_located(self.locator_1))
        logging.info(f"Found presence of the elements: {elements}")
        return elements

    def visibility_located(self):
        logging.info(f"Finding visibility of an element with a locator: {self.locator_1}")
        element = self.wait(self.driver, self.timeout).until(self.ec.visibility_of_element_located(self.locator_1))
        logging.info("Element is visible")
        return element

    def get_attribute(self):
        logging.info(f"Getting attribute '{self.attribute}' from an element with a locator: {self.locator_1}")
        element = self.wait(self.driver, self.timeout).until(self.ec.presence_of_element_located(self.locator_1))
        value = element.get_attribute(self.attribute)
        logging.info(f"Retrieved attribute '{self.attribute}': {value}")
        return value

    def right_click(self):
        logging.info(f"Right clicking on an element with a locator: {self.locator_1}")
        element = self.wait(self.driver, self.timeout).until(self.ec.element_to_be_clickable(self.locator_1))
        action_chains = ActionChains(self.driver)
        action_chains.context_click(element).perform()
        logging.info("Right clicked")

    def hover_over_element(self):
        logging.info(f"Hovering on an element with a locator: {self.locator_1}")
        element = self.wait(self.driver, self.timeout).until(self.ec.visibility_of_element_located(self.locator_1))
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(element).perform()
        logging.info("Hovered over the element")

    def scroll_to_element(self):
        logging.info(f"Scrolling to the element with a locator {self.locator_1}")
        element = self.wait(self.driver, self.timeout).until(self.ec.presence_of_element_located(self.locator_1))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        logging.info(f"Scrolled to the element with locator")

    def scroll_down(self):
        logging.info("Scrolling down")
        element = self.wait(self.driver, self.timeout).until(self.ec.presence_of_element_located(self.locator_1))
        element.send_keys(Keys.PAGE_DOWN)
        logging.info("Scrolled down")

