from selenium.webdriver.common.by import By
from base_page import BasePage
from elements.button_element import ButtonElement
from elements.alert_element import AlertElement
from elements.label_element import LabelElement


class Page1(BasePage):
    UNIQUE_ELEMENT_LOC = (By.ID, 'page-footer')
    BUTTON_JS_ALERT = (By.XPATH, '//button[@onclick="jsAlert()"]')
    BUTTON_JS_CONFIRM = (By.XPATH, '//button[@onclick="jsConfirm()"]')
    BUTTON_JS_PROMPT = (By.XPATH, '//button[@onclick="jsPrompt()"]')
    RESULT_ID = (By.ID, 'result')

    def __init__(self, driver):
        unique_element = LabelElement(driver, self.UNIQUE_ELEMENT_LOC)
        super().__init__(driver, unique_element)
        self.button_1 = ButtonElement(driver, self.BUTTON_JS_ALERT)
        self.button_2 = ButtonElement(driver, self.BUTTON_JS_CONFIRM)
        self.button_3 = ButtonElement(driver, self.BUTTON_JS_PROMPT)
        self.label = LabelElement(driver, self.RESULT_ID)
        self.alert = AlertElement(driver)
