from selenium.webdriver.common.by import By
from base_page.base_page import BasePage
from elements.label_element import LabelElement
from bs4 import BeautifulSoup


class Page1(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, '//div[contains(@class, "example")]')
    BS_FEATURE = 'html.parser'
    BS_NAME_TAG = 'div'
    BS_ATTRIBUTE = 'jscroll-added'

    def __init__(self, driver):
        unique_element = LabelElement(driver, self.UNIQUE_ELEMENT_LOC)
        super().__init__(driver, unique_element)

    def find_all(self):
        page_source = self.driver.page_source()
        soup = BeautifulSoup(page_source, self.BS_FEATURE)
        paragraphs = soup.find_all(self.BS_NAME_TAG, class_=self.BS_ATTRIBUTE)
        return paragraphs

