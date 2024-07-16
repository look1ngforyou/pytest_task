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
class TestAlertsContextClick:

    def setup_method(self):
        alerts_cc_data = self.test_data["alerts_cc_test"]
        self.url = alerts_cc_data["URL"]
        self.unique_element = (By.ID, 'hot-spot')
        self.result_cc = alerts_cc_data["RESULT_CLICK_ALERT_TEXT"]

    def test_alert_cc(self):
        self.browser.get_url(self.url)
        assert self.label_element.presence_located(self.unique_element), "Failed to open the page"
        logging.warning("Successfully opened the page")

        self.button_element.right_click(self.unique_element)
        assert self.alert_element.alert_text() in self.result_cc, "Failed to right-click on the element"
        logging.warning("Right-clicked on the element")

        self.alert_element.accept_alert()
        assert not self.alert_element.presence_of_alert(), "The Alert did not close"
        logging.warning("The Alert closed")