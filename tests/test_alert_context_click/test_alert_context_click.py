import pytest
import logging
from tests.test_alert_context_click.page1 import Page1
from browser.browser import Browser
from logging_configuration.logger import setup_logging


@pytest.fixture
def browser():
    setup_logging()
    browser = Browser("chrome")

    yield browser
    browser.quit()


class TestAlertContextClick:
    URL = "http://the-internet.herokuapp.com/context_menu"
    RESULT_CLICK_ALERT_TEXT = "You selected a context menu"

    def test(self, browser):
        logging.warning("Executing an alert test")
        self.page_1 = Page1(browser)

        browser.get(self.URL)
        self.page_1.wait_for_open()

        self.page_1.web_element.right_click()
        alert_window = browser.switch_to_alert()

        assert self.page_1.alert.presence_of_alert() is True, "Alert is not displayed"

        alert_text = self.page_1.alert.alert_text(alert_window)

        assert alert_text == self.RESULT_CLICK_ALERT_TEXT,\
            f"The required text {alert_text} is not expected {self.RESULT_CLICK_ALERT_TEXT}"
        self.page_1.alert.accept_alert(alert_window)

        assert self.page_1.alert.presence_of_alert() is False, "The Alert did not close"
        logging.warning("Successful interaction with an alert")
