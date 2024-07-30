from selenium.webdriver.common.by import By
from base_page.base_page import BasePage
from elements.label_element import LabelElement
from elements.button_element import ButtonElement


class Page1(BasePage):
    UNIQUE_ELEMENT_LOC = (By.ID, 'page-footer')
    BUTTON_LOC = (By.XPATH, '//div[contains(@class,"example")]//a')

    def __init__(self, driver):
        unique_element = LabelElement(driver, self.UNIQUE_ELEMENT_LOC)
        super().__init__(driver, unique_element)
        self.button = ButtonElement(driver, self.BUTTON_LOC, description="Handlers Page -> Redirection Button")

    def click(self):
        self.button.click()
