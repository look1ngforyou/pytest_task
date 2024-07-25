from selenium.webdriver.common.by import By
from base_page import BasePage
from elements.label_element import LabelElement
from elements.web_element import WebElement


class Page1(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, '//div[contains(@class, "example")]')
    PARAGRAPH_LOC = (By.XPATH, '//div[contains(@class, "jscroll-added")]')
    PAGE_LOC = (By.XPATH, '//body')

    def __init__(self, driver):
        unique_element = LabelElement(driver, self.UNIQUE_ELEMENT_LOC)
        super().__init__(driver, unique_element)
        self.paragraphs = LabelElement(driver, self.PARAGRAPH_LOC)
        self.web_element_1 = WebElement(driver, self.PAGE_LOC)

    def get_paragraph_count(self):
        paragraphs = self.paragraphs.presence_of_elements_located()
        return len(paragraphs)

    def scroll_down(self):
        self.web_element_1.scroll_down()
