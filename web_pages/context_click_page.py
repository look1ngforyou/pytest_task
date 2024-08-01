from selenium.webdriver.common.by import By
from base_page.base_page import BasePage
from elements.web_element import WebElement
from elements.label_element import LabelElement


class Page1(BasePage):
    UNIQUE_ELEMENT_LOC = (By.ID, 'page-footer')
    CONTEXT_MENU_LOC = (By.ID, 'hot-spot')

    def __init__(self, driver):
        unique_element = LabelElement(driver, self.UNIQUE_ELEMENT_LOC)
        super().__init__(driver, unique_element)
        self.web_element = WebElement(driver, self.CONTEXT_MENU_LOC, description="Context Menu Page -> Window")

    def right_click_on_window(self):
        self.web_element.right_click()
