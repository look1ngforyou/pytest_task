from selenium.webdriver.common.by import By
from base_page.base_page import BasePage
from elements.label_element import LabelElement
from elements.web_element import WebElement


class Page1(BasePage):
    UNIQUE_ELEMENT_LOC = (By.ID, 'page-footer')
    FIGURE_TEMPLATE = '(//div[contains(@class,"figure")])[{}]'
    CAPTION_TEMPLATE = '(//div[contains(@class,"figcaption")])[{}]/h5'
    PROFILE_LABEL_TEMPLATE = '(//div[contains(@class,"figcaption")])[{}]//a'

    def __init__(self, driver):
        unique_element = LabelElement(driver, self.UNIQUE_ELEMENT_LOC)
        super().__init__(driver, unique_element)

    def hover_over_figure(self, index):
        figure_template = (By.XPATH, self.FIGURE_TEMPLATE.format(index))
        figure = WebElement(self.driver, figure_template, description="Hovers Page -> Figure Template")
        figure.hover_over_element()

    def get_caption_text(self, index):
        caption_template = (By.XPATH, self.CAPTION_TEMPLATE.format(index))
        caption = LabelElement(self.driver, caption_template, description="Hovers Page -> Caption Template")
        return caption.text

    def click_profile_label(self, index):
        profile_label_template = (By.XPATH, self.PROFILE_LABEL_TEMPLATE.format(index))
        profile_label = LabelElement(self.driver, profile_label_template, description="Hovers Page -> Profile Template")
        profile_label.click()
