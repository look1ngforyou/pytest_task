import logging
from web_pages.context_menu_page import Page1


class TestAlertContextClick:
    URL = "https://the-internet.herokuapp.com/context_menu"
    RESULT_CLICK_ALERT_TEXT = "You selected a context menu"

    def test(self, browser):
        logger = logging.getLogger('logger')
        logger.info("Executing an alert test")
        self.page_1 = Page1(browser)

        browser.get(self.URL)
        self.page_1.wait_for_open()

        self.page_1.right_click()

        alert_window = browser.switch_to_alert()

        assert browser.is_alert_present() is True, "Alert is not displayed"

        alert_text = browser.alert_text(alert_window)

        assert alert_text == self.RESULT_CLICK_ALERT_TEXT, \
            f"The required text {alert_text} is not expected {self.RESULT_CLICK_ALERT_TEXT}"
        browser.accept_alert(alert_window)

        assert browser.is_alert_present() is False, "The Alert did not close"
