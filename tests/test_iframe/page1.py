from selenium.webdriver.common.by import By
from base_page import BasePage
from elements.label_element import LabelElement
from elements.web_element import WebElement


class Page1(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//footer")
    NESTED_FRAMES = (By.XPATH, "//span[text()='Nested Frames']")
    NESTED_FRAMES_TITLE = (By.XPATH, '//h1[contains(@class, "text-center")]')

    PARENT_FRAME_LOC = (By.ID, 'frame1')
    TEXT_INSIDE_PFRAME_lOC = (By.XPATH, '//body[normalize-space(.)="Parent frame"]')

    CHILD_IFRAME_LOC = (By.XPATH, '//iframe[@srcdoc]')
    TEXT_INSIDE_IFRAME_LOC = (By.XPATH, '//body[normalize-space(.)="Child Iframe"]')

    def __init__(self, driver):
        unique_element = LabelElement(driver, self.UNIQUE_ELEMENT_LOC)
        super().__init__(driver, unique_element)

        self.label = LabelElement(driver, self.NESTED_FRAMES)
        self.title = LabelElement(driver, self.NESTED_FRAMES_TITLE)

        self.parent_frame = WebElement(driver, self.PARENT_FRAME_LOC)
        self.label_frame = LabelElement(driver, self.TEXT_INSIDE_PFRAME_lOC)

        self.child_iframe = WebElement(driver, self.CHILD_IFRAME_LOC)
        self.label_iframe = LabelElement(driver, self.TEXT_INSIDE_IFRAME_LOC)
