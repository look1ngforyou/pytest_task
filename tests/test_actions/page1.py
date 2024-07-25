from selenium.webdriver.common.by import By
from elements.label_element import LabelElement
from elements.custom_elements.slider_element import SliderElement
from base_page import BasePage


class Page1(BasePage):
    UNIQUE_ELEMENT_LOC = (By.ID, 'page-footer')
    SLIDER_LOC = (By.XPATH, '//*[@type="range"]')
    SLIDER_VALUE_LOC = (By.ID, 'range')
    VALUE = 5

    def __init__(self, driver):
        unique_element = LabelElement(driver, self.UNIQUE_ELEMENT_LOC)
        super().__init__(driver, unique_element)
        self.slider = SliderElement(driver,self.SLIDER_LOC,direction="right",value=self.VALUE)
        self.label = LabelElement(driver, self.SLIDER_VALUE_LOC)
