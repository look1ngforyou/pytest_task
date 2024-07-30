from selenium.webdriver.common.by import By
from base_page.base_page import BasePage
from elements.button_element import ButtonElement
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
        self.button_1 = ButtonElement(driver, self.BUTTON_JS_ALERT,
                                      description="Alert Page -> JS Alert -> Alert button")
        self.button_2 = ButtonElement(driver, self.BUTTON_JS_CONFIRM,
                                      description="Alert Page -> JS Confirm -> Confirm button")
        self.button_3 = ButtonElement(driver, self.BUTTON_JS_PROMPT,
                                      description="Alert Page ->  JS Prompt -> Prompt button")
        self.label = LabelElement(driver, self.RESULT_ID, description="Alert Page -> Action result")

    def click_on_js_alert(self):
        self.button_1.click()

    def click_on_js_confirm(self):
        self.button_2.click()

    def click_on_js_prompt(self):
        self.button_3.click()

    def result_text(self):
        return self.label.text()

