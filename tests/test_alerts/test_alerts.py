import pytest
import logging
from web_pages.alerts_page import Page1
from config import config


class TestAlerts:
    RESULT_ALERT_CONFIRMATION_TEXT_1 = "I am a JS Alert"
    RESULT_CLICK_ALERT_TEXT_1 = "You successfully clicked an alert"
    RESULT_ALERT_CONFIRMATION_TEXT_2 = "I am a JS Confirm"
    RESULT_CLICK_ALERT_TEXT_2 = "You clicked: Ok"
    RESULT_ALERT_CONFIRMATION_TEXT_3 = "I am a JS prompt"

    def test_js_alert(self, browser):
        logger = logging.getLogger('logger')
        logger.info("Execute an alert test")
        browser.get(config.ALERTS_URL)

        self.AlertPage = Page1(browser)
        self.AlertPage.wait_for_open()

        self.AlertPage.click_on_js_alert()

        actual_result_text = browser.get_alert_text()
        assert actual_result_text == self.RESULT_ALERT_CONFIRMATION_TEXT_1, \
            f"The required text {actual_result_text} is not expected {self.RESULT_ALERT_CONFIRMATION_TEXT_1}"
        browser.accept_alert()

        actual_result_text = self.AlertPage.get_result_text()
        assert actual_result_text == self.RESULT_CLICK_ALERT_TEXT_1, \
            f"The required text {actual_result_text} is not expected {self.RESULT_CLICK_ALERT_TEXT_1}"

    def test_js_confirm(self, browser):
        logger = logging.getLogger('logger')
        logger.info("Execute an alert test")
        browser.get(config.ALERTS_URL)

        self.AlertPage = Page1(browser)
        self.AlertPage.wait_for_open()

        self.AlertPage.click_on_js_confirm()

        actual_result_text = browser.get_alert_text()
        assert actual_result_text == self.RESULT_ALERT_CONFIRMATION_TEXT_2, \
            f"The required text {actual_result_text} is not expected {self.RESULT_ALERT_CONFIRMATION_TEXT_2}"
        browser.accept_alert()

        actual_result_text = self.AlertPage.get_result_text()
        assert actual_result_text == self.RESULT_CLICK_ALERT_TEXT_2, \
            f"The required text {actual_result_text} is not expected {self.RESULT_CLICK_ALERT_TEXT_2}"

    @pytest.mark.parametrize("input_word, expected_result_text", [("word", "You entered: word")])
    def test_js_prompt(self, browser, input_word, expected_result_text):
        logger = logging.getLogger('logger')
        logger.info("Execute an alert test")
        browser.get(config.ALERTS_URL)

        self.AlertPage = Page1(browser)
        self.AlertPage.wait_for_open()

        self.AlertPage.click_on_js_prompt()

        actual_result_text = browser.get_alert_text()
        assert actual_result_text == self.RESULT_ALERT_CONFIRMATION_TEXT_3, \
            f"The required text {actual_result_text} is not expected {self.RESULT_ALERT_CONFIRMATION_TEXT_3}"
        browser.send_keys_to_alert(input_word)
        browser.accept_alert()

        actual_result_text = self.AlertPage.get_result_text()
        assert actual_result_text == expected_result_text, \
            f"The required text {actual_result_text} is not expected {expected_result_text}"
