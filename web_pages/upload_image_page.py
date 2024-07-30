from selenium.webdriver.common.by import By
from base_page.base_page import BasePage
from elements.label_element import LabelElement
from elements.button_element import ButtonElement
from elements.input_element import InputElement


class Page1(BasePage):
    UNIQUE_ELEMENT_LOC = (By.ID, 'page-footer')
    IMG_BUTTON_LOC = (By.ID, 'file-upload')
    UPLOAD_IMG_BUTTON_LOC = (By.ID, 'file-submit')
    UPLOADED_FILE_TEXT_LOC = (By.ID, 'uploaded-files')

    def __init__(self, driver):
        unique_element = LabelElement(driver, self.UNIQUE_ELEMENT_LOC)
        super().__init__(driver, unique_element)
        self.button = ButtonElement(driver, self.UPLOAD_IMG_BUTTON_LOC,
                                    description="Upload Image Page -> Upload Button")
        self.input = InputElement(driver, self.IMG_BUTTON_LOC, description="Upload Image Page -> Unload Button")
        self.label = LabelElement(driver, self.UPLOADED_FILE_TEXT_LOC, description="Upload Image Page -> Uploaded file")

    def send_keys(self, image):
        self.input.send_keys(image)

    def click(self):
        self.button.click()

    def text(self):
        return self.label.text()
