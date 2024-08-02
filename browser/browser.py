from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from browser_factory.browser_factory import BrowserFactory
import logging

logger = logging.getLogger('logger')


class Browser:
    TIMEOUT = 15

    def __init__(self, browser_type, arguments):
        logger.info(f"Initialize the browser with type: {browser_type}")
        self._driver = BrowserFactory.get_driver(browser_type=browser_type, arguments=arguments)

    @property
    def get_driver(self):
        return self._driver

    def get(self, url):
        logger.info(f"Navigate to the URL with address: {url}")
        self._driver.get(url)

    def quit(self):
        logger.info("Close the browser")
        self._driver.quit()

    def get_current_url(self):
        logger.info("Get the current URL address")
        current_url = self._driver.current_url
        return current_url

    def back(self):
        logger.info("Navigate to the previous URL")
        self._driver.back()

    def get_title(self):
        logger.info("Get the page title")
        title = self._driver.title
        logger.info(f"The page title is {title}")
        return title

    def close(self):
        logger.info("Close the current page")
        self._driver.close()

    def refresh(self):
        logger.info("Refresh thr current page")
        self._driver.refresh()

    def execute_script(self, script, *args):
        logger.info(f"Execute JavaScript {script} with the arguments {args}")
        result = self._driver.execute_script(script, *args)
        return result

    def get_page_source(self):
        logger.info("Get page source")
        source = self._driver.page_source
        return source

    def get_current_window_handle(self):
        logger.info("Get current window handle")
        current_handle = self._driver.current_window_handle
        return current_handle

    def switch_to_the_tab(self, current_window_handle):
        logger.info("Switch to the new tab with handle")
        new_window_handle = None
        for handle in self._driver.window_handles:
            if handle != current_window_handle:
                new_window_handle = handle
                break
        self._driver.switch_to.window(new_window_handle)

    def switch_to_iframe(self, iframe_loc):
        logger.info(f"Switch to an iframe {iframe_loc}")
        self._driver.switch_to.frame(iframe_loc)

    def switch_to_window(self, window_handle):
        logger.info(f"Switch to the window")
        self._driver.switch_to.window(window_handle)

    def close_tab_by_title(self, title):
        logger.info(f"Close the tab with the title: {title}")
        for handle in self._driver.window_handles:
            self._driver.switch_to.window(handle)
            if self.get_title() == title:
                self.close()
                break

    def _switch_to_alert(self):
        logger.info("Switch to an alert")
        WebDriverWait(self._driver, self.TIMEOUT).until(expected_conditions.alert_is_present())
        alert = self._driver.switch_to.alert
        return alert

    def get_alert_text(self):
        logger.info("Get an alert text")
        alert = self._switch_to_alert()
        text = alert.text
        logger.info(f"Received text: {text}")
        return text

    def accept_alert(self):
        logger.info("Accept an alert")
        alert = self._switch_to_alert()
        alert.accept()

    def deny_alert(self):
        logger.info("Dismiss an alert")
        alert = self._switch_to_alert()
        alert.dismiss()

    def send_keys_to_alert(self, value):
        logger.info(f"Send keys: {value} in the alert")
        alert = self._switch_to_alert()
        alert.send_keys(value)
