from browser_setting.browser_factory import BrowserFactory
import logging

logging.basicConfig(
    filename='test.log',
    level=logging.INFO,
    filemode="w",
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class Browser:
    def __init__(self, browser_type="chrome"):
        self.driver = BrowserFactory.get_driver(browser_type)
        logging.info(f"Initialized browser with type: {browser_type}")

    def get_url(self, url):
        self.driver.get(url)
        logging.info(f"Navigated to URL: {url}")

    def quit(self):
        self.driver.quit()
        logging.info("Closed the browser")

    def get_current_url(self):
        current_url = self.driver.current_url
        logging.info(f"Current URL: {current_url}")
        return current_url

    def back_to_previous_url(self):
        self.driver.back()
        logging.info("Navigated back to the previous URL")

    def get_page_title(self):
        title = self.driver.title
        logging.info(f"Page title: {title}")
        return title

    def close_page(self):
        self.driver.close()
        logging.info("Closed the current page")

    def refresh_page(self):
        self.driver.refresh()
        logging.info("Refreshed the current page")

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        logging.info(f"Scrolled to element with locator: {locator}")

    def scroll_to_defined_value(self, value):
        self.driver.execute_script(f"window.scrollBy(0, {value});")
        logging.info(f"Scrolled to defined value: {value}")

    def switch_to_new_tab(self, current_window_handle):
        new_window_handle = None
        for handle in self.driver.window_handles:
            if handle != current_window_handle:
                new_window_handle = handle
                break
        self.driver.switch_to.window(new_window_handle)
        logging.info(f"Switched to new tab with handle: {new_window_handle}")
        return new_window_handle

    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)
        logging.info(f"Switched to window with handle: {window_handle}")

    def close_tab_by_title(self, title):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == title:
                self.driver.close()
                logging.info(f"Closed tab with title: {title}")
                break

    def verify_text_present(self, by, locator, text):
        element = self.driver.find_element(by, locator)
        assert text in element.text
        logging.info(f"Verified text '{text}' is present in element with locator: {locator}")