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
class TestAuthorization:
    def setup_method(self):
        basic_auth_data = self.test_data["basic_authorization_test"]
        self.url = basic_auth_data["URL"].format(basic_auth_data["login"], basic_auth_data["password"])
        self.unique_element = (By.XPATH, '//div[contains(@class, "example")]')
        self.expected_text = basic_auth_data["AUTHORIZATION_TEXT"]

    def test_authorization(self):
        self.browser.get_url(self.url)
        text = self.web_element.get_text(self.unique_element)
        assert self.expected_text in text, 'Unsuccessful authorization'
        logging.warning("Successful authorization")
