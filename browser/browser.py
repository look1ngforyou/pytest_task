from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from browser_factory.browser_factory import BrowserFactory
import logging

logger = logging.getLogger('logger')


class Browser:
    TIMEOUT = 15

    def __init__(self, browser_type, arguments):
        logger.info(f"Initializing the browser with type: {browser_type}")
        self.driver = BrowserFactory.get_driver(browser_type=browser_type, arguments=arguments)

    def _get_driver(self):
        return self.driver

    def get(self, url):
        logger.info(f"Navigating to the URL with address: {url}")
        self.driver.get(url)

    def quit(self):
        logger.info("Closing the browser")
        self.driver.quit()

    def get_current_url(self):
        logger.info("Getting the current URL address")
        current_url = self.driver.current_url
        return current_url

    def back(self):
        logger.info("Navigating to the previous URL")
        self.driver.back()

    def get_title(self):
        logger.info("Getting the page title")
        title = self.driver.title
        logger.info(f"The page title is {title}")
        return title

    def close(self):
        logger.info("Closing the current page")
        self.driver.close()

    def refresh(self):
        logger.info("Refreshing thr current page")
        self.driver.refresh()

    def execute_script(self, script, *args):
        logger.info(f"Executing JavaScript {script} with the arguments {args}")
        result = self.driver.execute_script(script, *args)
        return result

    def get_page_source(self):
        logger.info("Getting page source")
        source = self.driver.page_source
        return source

    def get_current_window_handle(self):
        logger.info("Getting current window handle")
        current_handle = self.driver.current_window_handle
        return current_handle

    def switch_to_the_tab(self, current_window_handle):
        logger.info("Switching to the new tab with handle")
        new_window_handle = None
        for handle in self.driver.window_handles:
            if handle != current_window_handle:
                new_window_handle = handle
                break
        self.driver.switch_to.window(new_window_handle)

    def switch_to_iframe(self, iframe_loc):
        logger.info(f"Switching to an iframe {iframe_loc}")
        self.driver.switch_to.frame(iframe_loc)

    def switch_to_window(self, window_handle):
        logger.info(f"Switching to the window")
        self.driver.switch_to.window(window_handle)

    def close_tab_by_title(self, title):
        logger.info(f"Closing the tab with the title: {title}")
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.get_title() == title:
                self.close()
                break

    def switch_to_alert(self):
        logger.info("Switching to an alert")
        WebDriverWait(self.driver, self.TIMEOUT).until(expected_conditions.alert_is_present())
        alert = self.driver.switch_to.alert
        return alert

    def get_alert_text(self):
        logger.info("Getting an alert text")
        alert = self.switch_to_alert()
        text = alert.text
        logger.info(f"Received text: {text}")
        return text

    def accept_alert(self):
        logger.info("Accepting an alert")
        alert = self.switch_to_alert()
        alert.accept()

    def deny_alert(self, alert_window):
        logger.info("Dismissing an alert")
        alert = self.switch_to_alert()
        alert.dismiss()

    def alert_send_keys(self, value):
        logger.info(f"Sending keys: {value} in the alert")
        alert = self.switch_to_alert()
        alert.send_keys(value)

