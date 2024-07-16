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
class TestUploadImage:
    def setup_method(self):
        upload_image_data = self.test_data["upload_image"]
        self.url = upload_image_data["URL"]
        self.unique_element = (By.XPATH, '//div[contains(@class, "example")]')
        self.choose_image_button = (By.XPATH, '//*[@id="file-upload"]')
        self.upload_image_button = (By.ID, 'file-submit')
        self.uploaded_files_text = (By.ID, 'uploaded-files')
        self.photo_location = upload_image_data["photo"]
        self.photo_name = upload_image_data["photo_name"]

    def test_upload_image(self):
        self.browser.get_url(self.url)
        assert self.label_element.presence_located(self.unique_element), 'Failed to open the main page'
        logging.warning("Successfully opened the main page")

        file_input = self.button_element.presence_located(self.choose_image_button)
        file_input.send_keys(self.photo_location)

        self.button_element.click_on_element(self.upload_image_button)
        assert self.label_element.get_text(self.uploaded_files_text) == self.photo_name, "The file name did not appear"
        logging.warning("The file name has appeared")
