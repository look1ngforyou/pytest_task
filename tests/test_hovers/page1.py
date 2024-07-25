from selenium.webdriver.common.by import By
from base_page import BasePage
from elements.label_element import LabelElement
from elements.web_element import WebElement


class Page1(BasePage):
    UNIQUE_ELEMENT_LOC = (By.ID, 'page-footer')

    def __init__(self, driver):
        unique_element = LabelElement(driver, self.UNIQUE_ELEMENT_LOC)
        super().__init__(driver, unique_element)

    def get_figure(self, index):
        figure_template = (By.XPATH, f'(//div[contains(@class,"figure")])[{index}]')
        return WebElement(self.driver, figure_template)

    def get_caption(self, index):
        caption_template = (By.XPATH, f'(//div[contains(@class,"figcaption")])[{index}]/h5')
        return LabelElement(self.driver, caption_template)

    def get_profile_label(self, index):
        profile_label_template = (By.XPATH, f'(//div[contains(@class,"figcaption")])[{index}]//a')
        return LabelElement(self.driver, profile_label_template)

