from selenium.webdriver.common.by import By
from base_page.base_page import BasePage
from elements.label_element import LabelElement
from elements.image_element import ImageElement


class Page1(BasePage):
    UNIQUE_ELEMENT_LOC = (By.ID, 'page-footer')
    IMG_1_LOC = (By.XPATH, '(//div[contains(@class, "large-2 columns")]/img) [1]')
    IMG_2_LOC = (By.XPATH, '(//div[contains(@class, "large-2 columns")]/img)[2]')
    IMG_3_LOC = (By.XPATH, '(//div[contains(@class, "large-2 columns")]/img)[3]')
    ATTRIBUTE = 'src'

    def __init__(self, driver):
        unique_element = LabelElement(driver, self.UNIQUE_ELEMENT_LOC)
        super().__init__(driver, unique_element)
        self.image_1 = ImageElement(driver, self.IMG_1_LOC, description="Dynamic content Page -> Image_1")
        self.image_2 = ImageElement(driver, self.IMG_2_LOC, description="Dynamic content Page -> Image_2")
        self.image_3 = ImageElement(driver, self.IMG_3_LOC, description="Dynamic content Page -> Image_3")

    def get_image_1_attribute(self):
        return self.image_1.get_attribute(self.ATTRIBUTE)

    def get_image_2_attribute(self):
        return self.image_2.get_attribute(self.ATTRIBUTE)

    def get_image_3_attribute(self):
        return self.image_3.get_attribute(self.ATTRIBUTE)