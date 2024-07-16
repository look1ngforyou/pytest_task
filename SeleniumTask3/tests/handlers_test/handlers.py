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
class TestHandlers:
    def setup_method(self):
        self.handlers_data = self.test_data["handlers"]
        self.url = self.handlers_data["URL"]
        self.unique_element = (By.XPATH, '//div[contains(@class, "example")]')
        self.button = (By.XPATH, '//div[contains(@class,"example")]//a')
        self.new_window_text = "New Window"
        self.assertion_text = self.handlers_data["ASSERTION_TEXT"]
        self.browser_tab_name = (By.TAG_NAME, 'body', 'New Window')

    def test_transfer(self):
        self.browser.get_url(self.url)
        assert self.label_element.presence_located(self.unique_element), 'Failed to open the main page'
        logging.warning("Successfully opened the main page")

        main_window = self.browser.driver.current_window_handle

        self.button_element.click_on_element(self.button)
        self.browser.switch_to_new_tab(main_window)

        assert self.browser.get_page_title() == self.new_window_text, "A new tab did not open"
        logging.warning("The new tab has opened")
        self.browser.verify_text_present(By.TAG_NAME, 'body', 'New Window')

        self.browser.switch_to_window(main_window)
        assert self.web_element.presence_located(self.unique_element), "Failed to switch back to the main window"
        logging.warning("Successfully switched back to the main window")

        self.button_element.click_on_element(self.button)
        self.browser.switch_to_new_tab(main_window)
        assert self.browser.get_page_title() == self.new_window_text, "A new tab did not open"
        logging.warning("New tab has opened")
        self.browser.verify_text_present(By.TAG_NAME, 'body', 'New Window')

        self.browser.switch_to_window(main_window)
        assert self.web_element.presence_located(self.unique_element), "Failed to switch back to the main window"
        logging.warning("Successfully switched back to the main window")

        self.browser.close_tab_by_title(self.new_window_text), "Failed to close the new tab"
        logging.warning("The new tab was successfully closed")
        self.browser.close_tab_by_title(self.new_window_text), "Failed to close the new tab"
        logging.warning("The new tab was successfully closed again")