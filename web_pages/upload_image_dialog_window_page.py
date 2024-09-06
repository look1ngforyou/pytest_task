from selenium.webdriver.common.by import By
from base_page.base_page import BasePage
from elements.label_element import LabelElement
from elements.web_element import WebElement


class Page1(BasePage):
    UNIQUE_ELEMENT_LOC = (By.ID, 'page-footer')
    IMG_BUTTON_LOC = (By.ID, 'drag-drop-upload')
    UPLOADED_FILE_TEXT_LOC = (By.XPATH, '(//div[contains(@class, "dz-filename")])[1]//span')
    CHECK_MARK_SYMBOL_LOC = (By.XPATH, '(//div[contains(@class, "dz-success-mark")])[2]//span')

    def __init__(self, driver):
        unique_element = LabelElement(driver, self.UNIQUE_ELEMENT_LOC)
        super().__init__(driver, unique_element)
        self.web_element_1 = WebElement(driver, self.IMG_BUTTON_LOC, description="Image Upload Page -> Upload Window")
        self.label = LabelElement(driver, self.UPLOADED_FILE_TEXT_LOC, description="Image Upload Page -> Uploaded file")
        self.web_element_2 = WebElement(driver, self.CHECK_MARK_SYMBOL_LOC,
                                        description="Image Upload Page -> Check mark")

    def click_to_submit_image(self):
        self.web_element_1.click()

    def upload_image_via_fe(self, file_path):
        self.click_to_submit_image()

    def get_image_text(self):
        return self.label.text

    def presence_of_check_mark_located(self):
        return self.web_element_2.get_presence_of_element_located()
