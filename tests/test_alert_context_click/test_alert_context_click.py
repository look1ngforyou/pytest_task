import logging
from web_pages.context_click_page import Page1
from config import config


class TestAlertContextClick:
    URL = config.ALERT_CC_URL
    RESULT_CLICK_ALERT_TEXT = "You selected a context menu"

    def test_alert_context_click(self, browser):
        logger = logging.getLogger('logger')
        logger.info("Executing an alert test")
        browser.get(self.URL)

        self.page_1 = Page1(browser)
        self.page_1.wait_for_open()

        self.page_1.right_click_on_window()

        alert_text = browser.get_alert_text()

        assert alert_text == self.RESULT_CLICK_ALERT_TEXT, \
            f"The required text {alert_text} is not expected {self.RESULT_CLICK_ALERT_TEXT}"
        browser.accept_alert()

