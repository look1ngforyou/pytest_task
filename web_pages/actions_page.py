from selenium.webdriver.common.by import By
from elements.label_element import LabelElement
from elements.custom_elements.slider_element import SliderElement
from base_page.base_page import BasePage


class Page1(BasePage):
    UNIQUE_ELEMENT_LOC = (By.ID, 'page-footer')
    SLIDER_LOC = (By.XPATH, '//*[@type="range"]')
    SLIDER_VALUE_LOC = (By.ID, 'range')

    def __init__(self, driver):
        unique_element = LabelElement(driver, self.UNIQUE_ELEMENT_LOC)
        super().__init__(driver, unique_element)
        self.slider = SliderElement(driver, self.SLIDER_LOC, description="Slider Page -> Slider")
        self.label = LabelElement(driver, self.SLIDER_VALUE_LOC, description="Slider Page -> Slider Value")

    def move_slider(self, direction, value):
        self.slider.move_the_slider_to_the_trajectory(direction=direction,
                                                      value=value)

    def get_slider_value(self):
        real_value = float(self.label.text())
        return real_value
