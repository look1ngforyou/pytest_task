from selenium.webdriver.common.by import By
from base_page.base_page import BasePage
from elements.label_element import LabelElement
from bs4 import BeautifulSoup


class Page1(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, '//div[contains(@class, "example")]')

    def __init__(self, driver):
        unique_element = LabelElement(driver, self.UNIQUE_ELEMENT_LOC)
        super().__init__(driver, unique_element)

    def find_all(self):
        page_source = self.driver.get_page_source()
        soup = BeautifulSoup(page_source, 'html.parser')
        paragraphs = soup.find_all('div', class_='jscroll-added')
        return paragraphs
