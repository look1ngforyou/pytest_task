import pytest
import logging
from web_pages.alerts_page import Page1
from config import config


class TestAlerts:
    URL = config.ALERTS_URL
    ALERT_CONFIRMATION_TEXT_1 = "I am a JS Alert"
    RESULT_CLICK_ALERT_TEXT_1 = "You successfully clicked an alert"
    ALERT_CONFIRMATION_TEXT_2 = "I am a JS Confirm"
    RESULT_CLICK_ALERT_TEXT_2 = "You clicked: Ok"
    ALERT_CONFIRMATION_TEXT_3 = "I am a JS prompt"

    def test_js_alert(self, browser):
        logger = logging.getLogger('logger')
        logger.info("Executing an alert test")
        browser.get(self.URL)

        self.page_1 = Page1(browser)
        self.page_1.wait_for_open()

        self.page_1.click_on_js_alert()

        alert_text = browser.get_alert_text()
        assert alert_text == self.ALERT_CONFIRMATION_TEXT_1, \
            f"The required text {alert_text} is not expected {self.ALERT_CONFIRMATION_TEXT_1}"
        browser.accept_alert()

        result_text = self.page_1.result_text()
        assert result_text == self.RESULT_CLICK_ALERT_TEXT_1, \
            f"The required text {result_text} is not expected {self.RESULT_CLICK_ALERT_TEXT_1}"

    def test_js_confirm(self, browser):
        logger = logging.getLogger('logger')
        logger.info("Executing an alert test")
        browser.get(self.URL)

        self.page_1 = Page1(browser)
        self.page_1.wait_for_open()

        self.page_1.click_on_js_confirm()

        alert_text = browser.get_alert_text()
        assert alert_text == self.ALERT_CONFIRMATION_TEXT_2, \
            f"The required text {alert_text} is not expected {self.ALERT_CONFIRMATION_TEXT_2}"
        browser.accept_alert()

        result_text = self.page_1.result_text()
        assert result_text == self.RESULT_CLICK_ALERT_TEXT_2, \
            f"The required text {result_text} is not expected {self.RESULT_CLICK_ALERT_TEXT_2}"

    @pytest.mark.parametrize("word, result", [("word", "You entered: word")])
    def test_js_prompt(self, browser, word, result):
        logger = logging.getLogger('logger')
        logger.info("Executing an alert test")
        browser.get(self.URL)

        self.page_1 = Page1(browser)
        self.page_1.wait_for_open()

        self.page_1.click_on_js_prompt()

        alert_text = browser.get_alert_text()
        assert alert_text == self.ALERT_CONFIRMATION_TEXT_3, \
            f"The required text {alert_text} is not expected {self.ALERT_CONFIRMATION_TEXT_3}"
        browser.alert_send_keys(word)
        browser.accept_alert()

        result_text = self.page_1.result_text()
        assert result_text == result, \
            f"The required text {result_text} is not expected {result}"
