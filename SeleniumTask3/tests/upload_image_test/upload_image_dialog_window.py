import pytest
from selenium.webdriver.common.by import By
from tests.test_utilities.test_utils import upload_file_via_fe
import logging

logging.basicConfig(
    filename='../test.log',
    level=logging.INFO,
    filemode="w",
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


@pytest.mark.usefixtures("setup")
class TestUploadImage:
    def setup_method(self):
        upload_image_data = self.test_data["upload_image"]
        self.url = upload_image_data["URL"]
        self.unique_element = (By.XPATH, '//div[contains(@class, "example")]')
        self.upload_image_frame = (By.XPATH, '//div[contains(@class, "dz-success-mark dz-clickable")]')
        self.photo_location = upload_image_data["photo"]
        self.photo_text = (By.XPATH, '(//div[contains(@class, "dz-filename")])[1]//span')
        self.photo_name = upload_image_data["photo_name"]
        self.gap_symbol = (By.XPATH, '(//div[contains(@class, "dz-success-mark")])[2]//span')

    def test_upload_with_dialog_window(self):
        self.browser.get_url(self.url)
        assert self.label_element.presence_located(self.unique_element), 'Failed to open the main page'
        logging.warning("Successfully opened the main page")

        self.web_element.click_on_element(self.upload_image_frame)
        upload_file_via_fe(self.photo_location), "The dialogue tab has not opened"
        logging.warning("The dialogue tab has opened")

        assert self.label_element.get_text(self.photo_text), "The file name has not appeared"
        logging.warning("The file name has appeared")

        assert self.label_element.presence_located(self.gap_symbol), "The symbol has not appeared"
        logging.warning("The symbol has appeared")