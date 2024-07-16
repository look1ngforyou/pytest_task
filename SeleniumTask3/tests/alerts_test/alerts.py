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
class TestAlerts:
    def setup_method(self):
        alert_data = self.test_data["alerts_test"]
        self.url = alert_data["URL"]
        self.result_id = (By.ID, 'result')
        self.unique_element = (By.XPATH, '//div[contains(@class, "example")]')

        self.button_js_alert = (By.XPATH, '//button[@onclick="jsAlert()"]')
        self.button_js_confirm = (By.XPATH, '//button[@onclick="jsConfirm()"]')
        self.button_js_prompt = (By.XPATH, '//button[@onclick="jsPrompt()"]')

        self.alert_conf_text_1 = alert_data["ALERT_CONFIRMATION_TEXT_1"]
        self.result_text_1 = alert_data["RESULT_CLICK_ALERT_TEXT_1"]

        self.alert_conf_text_2 = alert_data["ALERT_CONFIRMATION_TEXT_2"]
        self.result_text_2 = alert_data["RESULT_CLICK_ALERT_TEXT_2"]

        self.alert_conf_text_3 = alert_data["ALERT_CONFIRMATION_TEXT_3"]
        self.result_text_3 = alert_data["RESULT_CLICK_ALERT_TEXT_3"]

    def test_js_alert(self):
        self.browser.get_url(self.url)
        assert self.label_element.presence_located(self.unique_element), 'Failed open the page'
        logging.warning("Successfully opened the page")

        self.button_element.click_on_element(self.button_js_alert)
        assert self.alert_element.alert_text() in self.alert_conf_text_1, "The text is not displayed"
        logging.warning("The text is successfully displayed")

        self.alert_element.accept_alert()
        assert not self.alert_element.presence_of_alert(), 'JS Alert did not disappear'
        logging.warning("JS Alert has disappeared")

        assert self.label_element.get_text(self.result_id) in self.result_text_1, 'The required text is not displayed'
        logging.warning("Text is displayed")

    def test_js_confirm(self):
        self.browser.get_url(self.url)
        assert self.label_element.presence_located(self.unique_element), "Could not open the page"
        logging.warning("Successfully opened the page")

        self.button_element.click_on_element(self.button_js_confirm)
        assert self.alert_element.alert_text() in self.alert_conf_text_2, "The text is not displayed"
        logging.warning("Text is displayed")

        self.alert_element.accept_alert()
        assert not self.alert_element.presence_of_alert(), 'JS Alert did not disappear'
        logging.warning("JS Alert has disappeared")

        assert self.label_element.get_text(self.result_id) in self.result_text_2, 'The required text is not displayed'
        logging.warning("Text is displayed")

    def test_js_prompt(self):
        self.browser.get_url(self.url)
        assert self.label_element.presence_located(self.unique_element), 'Failed open the page'
        logging.warning("Successfully opened the page")

        self.button_element.click_on_element(self.button_js_prompt)
        assert self.alert_element.alert_text() in self.alert_conf_text_3, 'The text is not displayed'
        logging.warning("Text is displayed")

        self.alert_element.accept_alert()
        assert not self.alert_element.presence_of_alert(), 'JS Alert did not disappear'
        logging.warning("JS Alert has disappeared")

        assert self.label_element.get_text(self.result_id) in self.result_text_3, 'The required text is not displayed'
        logging.warning("Text is displayed")
