from selenium.webdriver.common.by import By
from base_page import BasePage
from elements.label_element import LabelElement
from elements.button_element import ButtonElement


class Page1(BasePage):
    UNIQUE_ELEMENT_LOC = (By.ID, 'page-footer')
    BUTTON_LOC = (By.XPATH, '//div[contains(@class,"example")]//a')
    PAGE_TEXT_LOC = (By.TAG_NAME, 'body', 'New Window')

    def __init__(self, driver):
        unique_element = LabelElement(driver, self.UNIQUE_ELEMENT_LOC)
        super().__init__(driver, unique_element)
        self.button = ButtonElement(driver, self.BUTTON_LOC)
        self.label = LabelElement(driver, self.PAGE_TEXT_LOC)
