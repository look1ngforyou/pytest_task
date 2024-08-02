from selenium.webdriver.common.by import By
from base_page.base_page import BasePage
from elements.label_element import LabelElement
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger('logger')


class Page1(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, '//div[contains(@class, "example")]')
    PARAGRAPH_LOC = "(//div[contains(@class, 'jscroll-added')])[{}]"

    def __init__(self, driver):
        unique_element = LabelElement(driver, self.UNIQUE_ELEMENT_LOC)
        super().__init__(driver, unique_element)

    def find_all_paragraphs(self):
        page_source = self.driver.get_page_source()
        soup = BeautifulSoup(page_source, 'html.parser')
        paragraphs = soup.find_all('div', class_='jscroll-added')
        return paragraphs

    def scroll_through_paragraphs_to_aimed_value(self, aiming_paragraph_value):
        while True:
            current_paragraphs = len(self.find_all_paragraphs())
            logger.info(f"Current paragraphs amount: {current_paragraphs}")
            if current_paragraphs >= aiming_paragraph_value:
                break

            locator = (By.XPATH, self.PARAGRAPH_LOC.format(current_paragraphs))
            last_paragraph = LabelElement(self.driver, locator, description="Infinite Scroll Page -> Paragraph")
            last_paragraph.scroll_into_view()

        return current_paragraphs

