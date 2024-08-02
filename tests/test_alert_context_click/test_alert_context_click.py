import logging
from web_pages.context_click_page import Page1
from config import config


class TestAlertContextClick:
    EXPECTED_RESULT_ALERT_TEXT = "You selected a context menu"

    def test_alert_context_click(self, browser):
        logger = logging.getLogger('logger')
        logger.info("Execute an alert test")
        browser.get(config.ALERT_CC_URL)

        self.AlertPage = Page1(browser)
        self.AlertPage.wait_for_open()

        self.AlertPage.right_click_on_window()

        actual_alert_text = browser.get_alert_text()

        assert actual_alert_text == self.EXPECTED_RESULT_ALERT_TEXT, \
            f"The required text {actual_alert_text} is not expected {self.EXPECTED_RESULT_ALERT_TEXT}"
        browser.accept_alert()

