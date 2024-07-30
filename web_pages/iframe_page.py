from selenium.webdriver.common.by import By
from base_page.base_page import BasePage
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

        self.label = LabelElement(driver, self.NESTED_FRAMES, description="Main Page -> Redirection button")
        self.title = LabelElement(driver, self.NESTED_FRAMES_TITLE, description="Frames Page -> Parent title")

        self.parent_frame = WebElement(driver, self.PARENT_FRAME_LOC, description="Frames Page -> Parent frame")
        self.label_frame = LabelElement(driver, self.TEXT_INSIDE_PFRAME_lOC,
                                        description="Frame Page -> Parent Frame text")

        self.child_iframe = WebElement(driver, self.CHILD_IFRAME_LOC, description="Frames Page -> Child iframe")
        self.label_iframe = LabelElement(driver, self.TEXT_INSIDE_IFRAME_LOC,
                                         description="Frames Page -> Child Frame text")

    def scroll_into_view(self):
        self.label.scroll_into_view()

    def click(self):
        self.label.click()

    def presence_of_title_located(self):
        return self.title.presence_of_element_located()

    def presence_of_parent_frame_located(self):
        return self.parent_frame.presence_of_element_located()

    def frame_text(self):
        return self.label_frame.text()

    def presence_of_child_iframe_located(self):
        return self.child_iframe.presence_of_element_located()

    def iframe_text(self):
        return self.label_iframe.text()
