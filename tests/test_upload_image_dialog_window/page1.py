from selenium.webdriver.common.by import By
from base_page import BasePage
from elements.label_element import LabelElement
from elements.button_element import ButtonElement
from elements.web_element import WebElement


class Page1(BasePage):
    UNIQUE_ELEMENT_LOC = (By.ID, 'page-footer')
    IMG_BUTTON_LOC = (By.XPATH, '//*[@id="drag-drop-upload"]')
    UPLOADED_FILE_TEXT_LOC = (By.XPATH, '(//div[contains(@class, "dz-filename")])[1]//span')
    GAP_SYMBOL_LOC = (By.XPATH, '(//div[contains(@class, "dz-success-mark")])[2]//span')

    def __init__(self, driver):
        unique_element = LabelElement(driver, self.UNIQUE_ELEMENT_LOC)
        super().__init__(driver, unique_element)
        self.web_element_1 = WebElement(driver, self.IMG_BUTTON_LOC)
        self.label = LabelElement(driver, self.UPLOADED_FILE_TEXT_LOC)
        self.web_element_2 = WebElement(driver, self.GAP_SYMBOL_LOC)