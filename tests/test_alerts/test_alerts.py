import logging
from web_pages.alerts_page import Page1


class TestAlerts:
    URL = "https://the-internet.herokuapp.com/javascript_alerts"
    ALERT_CONFIRMATION_TEXT_1 = "I am a JS Alert"
    RESULT_CLICK_ALERT_TEXT_1 = "You successfully clicked an alert"
    ALERT_CONFIRMATION_TEXT_2 = "I am a JS Confirm"
    RESULT_CLICK_ALERT_TEXT_2 = "You clicked: Ok"
    ALERT_CONFIRMATION_TEXT_3 = "I am a JS prompt"
    submit_keys = "word"
    result_click_alert_text = f"You entered: {submit_keys}"

    def test_js_alert(self, browser):
        logger = logging.getLogger('logger')
        logger.info("Executing an alert test")
        self.page_1 = Page1(browser)

        browser.get(self.URL)
        self.page_1.wait_for_open()

        self.page_1.click_on_js_alert()
        alert_window = browser.switch_to_alert()

        assert browser.is_alert_present() is True, "Alert is not displayed"

        alert_text = browser.alert_text(alert_window)
        assert alert_text == self.ALERT_CONFIRMATION_TEXT_1, \
            f"The required text {alert_text} is not expected {self.ALERT_CONFIRMATION_TEXT_1}"
        browser.accept_alert(alert_window)

        result_text = self.page_1.result_text()
        assert result_text == self.RESULT_CLICK_ALERT_TEXT_1, \
            f"The required text {result_text} is not expected {self.RESULT_CLICK_ALERT_TEXT_1}"

    def test_js_confirm(self, browser):
        logger = logging.getLogger('logger')
        logger.info("Executing an alert test")
        self.page_1 = Page1(browser)

        browser.get(self.URL)
        self.page_1.wait_for_open()

        self.page_1.click_on_js_confirm()
        alert_window = browser.switch_to_alert()

        assert browser.is_alert_present() is True, "Alert is not displayed"

        alert_text = browser.alert_text(alert_window)
        assert alert_text == self.ALERT_CONFIRMATION_TEXT_2, \
            f"The required text {alert_text} is not expected {self.ALERT_CONFIRMATION_TEXT_2}"
        browser.accept_alert(alert_window)

        result_text = self.page_1.result_text()
        assert result_text == self.RESULT_CLICK_ALERT_TEXT_2, \
            f"The required text {result_text} is not expected {self.RESULT_CLICK_ALERT_TEXT_2}"

    def test_js_prompt(self, browser):
        logger = logging.getLogger('logger')
        logger.info("Executing an alert test")
        self.page_1 = Page1(browser)

        browser.get(self.URL)
        self.page_1.wait_for_open()

        self.page_1.click_on_js_prompt()
        alert_window = browser.switch_to_alert()

        assert browser.is_alert_present() is True, "Alert is not displayed"

        alert_text = browser.alert_text(alert_window)
        assert alert_text == self.ALERT_CONFIRMATION_TEXT_3, \
            f"The required text {alert_text} is not expected {self.ALERT_CONFIRMATION_TEXT_3}"
        browser.alert_send_keys(alert_window, self.submit_keys)
        browser.accept_alert(alert_window)

        result_text = self.page_1.result_text()
        assert result_text == self.result_click_alert_text, \
            f"The required text {result_text} is not expected {self.result_click_alert_text}"
