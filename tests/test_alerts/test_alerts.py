import pytest
import logging
from tests.test_alerts.page1 import Page1
from browser.browser import Browser
from logging_configuration.logger import setup_logging


@pytest.fixture
def browser():
    setup_logging()
    browser = Browser("chrome")

    yield browser
    browser.quit()


class TestAlerts:
    URL = "https://the-internet.herokuapp.com/javascript_alerts"
    ALERT_CONFIRMATION_TEXT_1 = "I am a JS Alert"
    RESULT_CLICK_ALERT_TEXT_1 = "You successfully clicked an alert"
    ALERT_CONFIRMATION_TEXT_2 = "I am a JS Confirm"
    RESULT_CLICK_ALERT_TEXT_2 = "You clicked: Ok"
    ALERT_CONFIRMATION_TEXT_3 = "I am a JS prompt"
    SUBMIT_KEYS = "word"
    RESULT_CLICK_ALERT_TEXT_3 = f"You entered: {SUBMIT_KEYS}"

    def test_js_alert(self, browser):
        logging.warning("Executing an alert test")
        self.page_1 = Page1(browser)

        browser.get(self.URL)
        self.page_1.wait_for_open()

        self.page_1.button_1.click()
        alert_window = browser.switch_to_alert()

        assert self.page_1.alert.presence_of_alert() is True, "Alert is not displayed"

        alert_text = self.page_1.alert.alert_text(alert_window)
        assert alert_text == self.ALERT_CONFIRMATION_TEXT_1, \
            f"The required text {alert_text} is not expected {self.ALERT_CONFIRMATION_TEXT_1}"
        self.page_1.alert.accept_alert(alert_window)

        result_text = self.page_1.label.text()
        assert result_text == self.RESULT_CLICK_ALERT_TEXT_1, \
            f"The required text {result_text} is not expected {self.RESULT_CLICK_ALERT_TEXT_1}"
        logging.warning("Successful interaction with an alert")

    def test_js_confirm(self, browser):
        logging.warning("Executing an alert test")
        self.page_1 = Page1(browser)

        browser.get(self.URL)
        self.page_1.wait_for_open()

        self.page_1.button_2.click()
        alert_window = browser.switch_to_alert()

        assert self.page_1.alert.presence_of_alert() is True, "Alert is not displayed"

        alert_text = self.page_1.alert.alert_text(alert_window)
        assert alert_text == self.ALERT_CONFIRMATION_TEXT_2, \
            f"The required text {alert_text} is not expected {self.ALERT_CONFIRMATION_TEXT_2}"
        self.page_1.alert.accept_alert(alert_window)

        result_text = self.page_1.label.text()
        assert result_text == self.RESULT_CLICK_ALERT_TEXT_2, \
            f"The required text {result_text} is not expected {self.RESULT_CLICK_ALERT_TEXT_2}"
        logging.warning("Successful interaction with an alert")

    def test_js_prompt(self, browser):
        logging.warning("Executing an alert test")
        self.page_1 = Page1(browser)

        browser.get(self.URL)
        self.page_1.wait_for_open()

        self.page_1.button_3.click()
        alert_window = browser.switch_to_alert()

        assert self.page_1.alert.presence_of_alert() is True, "Alert is not displayed"

        alert_text = self.page_1.alert.alert_text(alert_window)
        assert alert_text == self.ALERT_CONFIRMATION_TEXT_3, \
            f"The required text {alert_text} is not expected {self.ALERT_CONFIRMATION_TEXT_3}"
        self.page_1.alert.alert_send_keys(alert_window, self.SUBMIT_KEYS)
        self.page_1.alert.accept_alert(alert_window)

        result_text = self.page_1.label.text()
        assert result_text == self.RESULT_CLICK_ALERT_TEXT_3, \
            f"The required text {result_text} is not expected {self.RESULT_CLICK_ALERT_TEXT_3}"
        logging.warning("Successful interaction with an alert")
