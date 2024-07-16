import pytest
from selenium.webdriver.common.by import By
import logging

logging.basicConfig(
    filename='../test.log',
    level=logging.INFO,
    filemode="w",
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


@pytest.mark.usefixtures("setup")
class TestIframe:
    def setup_method(self):
        iframe_data = self.test_data["iframe"]
        self.url = iframe_data["URL"]
        self.parent_text = iframe_data["parent_text"]
        self.child_text = iframe_data["child_text"]
        self.unique_element = (By.XPATH, '//div[contains(@class,"category-cards")]')
        self.frame_button = "https://demoqa.com/alertsWindows"
        self.click_for_nested_frames = (By.XPATH, "//span[text()='Nested Frames']")
        self.nested_frames_title = (By.XPATH, '//h1[contains(@class, "text-center")]')
        self.parent_frame_locator = (By.ID, 'frame1')
        self.element_inside_parent_frame_locator = (By.XPATH, '//body[normalize-space(.)="Parent frame"]')
        self.child_iframe_locator = (By.XPATH, '//iframe[@srcdoc]')
        self.element_inside_child_iframe_locator = (By.XPATH, '//body[normalize-space(.)="Child Iframe"]')

    def test_iframes(self):
        self.browser.get_url(self.url)
        assert self.label_element.presence_located(self.unique_element), 'Failed to open the main page'
        logging.warning("Successfully opened the main page")

        self.browser.get_url(self.frame_button)
        self.browser.scroll_to_element(self.click_for_nested_frames)
        self.label_element.click_on_element(self.click_for_nested_frames)
        assert self.label_element.presence_located(self.nested_frames_title), 'The inscriptions are not on the page'
        logging.warning('The inscriptions are on the page')

        parent_text = self.iframe_element.get_text_from_iframe(self.parent_frame_locator,
                                                               self.element_inside_parent_frame_locator)
        assert parent_text == self.parent_text, 'The text does not match the specified one'
        logging.warning('The text matches the specified one')

        child_text = self.iframe_element.get_text_from_nested_iframe(self.parent_frame_locator,
                                                                     self.child_iframe_locator,
                                                                     self.element_inside_child_iframe_locator)
        assert child_text == self.child_text, 'The text does not match the specified one'
        logging.warning('The text matches the specified one')
