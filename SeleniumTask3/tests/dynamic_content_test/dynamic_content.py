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
class TestDynamicContent:
    def setup_method(self):
        dc_data = self.test_data["dynamic_content"]
        self.url = dc_data["URL"]
        self.unique_element = (By.XPATH, '//div[contains(@class, "example")]')
        self.img_1 = (By.XPATH, '(//div[contains(@class, "large-2 columns")]/img) [1]')
        self.img_2 = (By.XPATH, '(//div[contains(@class, "large-2 columns")]/img)[2]')
        self.img_3 = (By.XPATH, '(//div[contains(@class, "large-2 columns")]/img)[3]')

    def test_dynamic_content(self):
        self.browser.get_url(self.url)
        assert self.label_element.presence_located(self.unique_element), 'Failed open the page'
        logging.warning("Successfully opened the page")

        image_1 = self.web_element.get_attribute(self.img_1, 'src')
        image_2 = self.web_element.get_attribute(self.img_2, 'src')
        image_3 = self.web_element.get_attribute(self.img_3, 'src')

        while len({image_1, image_2, image_3}) == 3:
            self.browser.refresh_page()
            image_1 = self.web_element.get_attribute(self.img_1, 'src')
            image_2 = self.web_element.get_attribute(self.img_2, 'src')
            image_3 = self.web_element.get_attribute(self.img_3, 'src')

        assert image_1 == image_2 or image_1 == image_3 or image_2 == image_3, "The images do not match"
        logging.warning("The images match")
