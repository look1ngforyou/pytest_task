from base_element_and_descendants.base_element import BaseElement
from browser_setting import browser


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.element = BaseElement(driver)
        self.browser = browser.Browser()
