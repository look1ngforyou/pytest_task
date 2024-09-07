from selenium.webdriver.common.by import By
from base_page.base_page import BasePage
from elements.label_element import LabelElement


class Page1(BasePage):
    UNIQUE_ELEMENT_LOC = (By.ID, 'page-footer')
    PAGE_TEXT_XPATH = (By.XPATH, '//div[contains(@class, "example")]/p')

    def __init__(self, driver):
        unique_element = LabelElement(driver, self.UNIQUE_ELEMENT_LOC)
        super().__init__(driver, unique_element)
        self.label_1 = LabelElement(driver, self.PAGE_TEXT_XPATH,
                                    description="Authorization Page -> Authorization text")

    def get_page_text(self):
        return self.label_1.text
