from tests.test_utilities.test_utils import move_slider_to_aiming_value
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
class TestAction:
    def setup_method(self):
        alert_cc = self.test_data["actions_test"]
        self.url = alert_cc["URL"]
        self.unique_element = (By.XPATH, '//div[contains(@class, "example")]')
        self.slider = (By.XPATH, '//*[@type="range"]')
        self.slider_value = (By.ID, 'range')
        self.aiming_value = alert_cc["aiming_value"]

    def test_actions(self):
        self.browser.get_url(self.url)
        assert self.label_element.presence_located(self.unique_element), "Failed to open the page"
        logging.warning("Successfully opened the page")

        move_slider_to_aiming_value(self.slider_element, self.slider, self.slider_value, self.aiming_value)

        new_value = self.slider_element.get_slider_value(self.slider)
        assert new_value == self.aiming_value, "Failed to move slider to aiming value"
        logging.warning("Successfully moved slider to the desired value")
