from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from browser_factory.browser_factory import BrowserFactory
import logging

logger = logging.getLogger('logger')


class Browser:
    TIMEOUT = 15

    def __init__(self, browser_type):
        logger.info(f"Initializing the browser with type: {browser_type}")
        self.driver = BrowserFactory.get_driver(browser_type)

    def get_driver(self):
        return self.driver

    def get(self, url):
        logger.info(f"Navigating to the URL with address: {url}")
        self.driver.get(url)

    def quit(self):
        logger.info("Closing the browser")
        self.driver.quit()

    def current_url(self):
        logger.info("Getting the current URL address")
        current_url = self.driver.current_url
        logger.info(f"Current URl is {current_url}")
        return current_url

    def back(self):
        logger.info("Navigating to the previous URL")
        self.driver.back()

    def title(self):
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
        logger.info("Executing JavaScript")
        result = self.driver.execute_script(script, *args)
        logger.info(f"Executed script {script} with the arguments {args}")
        return result

    def page_source(self):
        logger.info("Getting page source")
        source = self.driver.page_source
        return source

    def current_window_handle(self):
        logger.info("Getting current window handle")
        current_handle = self.driver.current_window_handle
        return current_handle

    def switch_to_new_tab(self, current_window_handle):
        logger.info("Switching to the new tab with handle")
        new_window_handle = None
        for handle in self.driver.window_handles:
            if handle != current_window_handle:
                new_window_handle = handle
                break
        self.driver.switch_to.window(new_window_handle)
        return new_window_handle

    def switch_to_iframe(self, iframe_loc):
        logger.info("Switching to an iframe")
        self.driver.switch_to.frame(iframe_loc)

    def switch_to_window(self, window_handle):
        logger.info(f"Switching to the window")
        self.driver.switch_to.window(window_handle)

    def switch_to_alert(self):
        logger.info("Switching to an alert")
        alert = self.driver.switch_to.alert
        return alert

    def close_tab_by_title(self, title):
        logger.info(f"Closing the tab with the title: {title}")
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.title() == title:
                self.close()
                logger.info(f"Closed the tab with the title {title}")
                break

    def alert_text(self, alert_window):
        logger.info("Getting an alert text")
        text = alert_window.text
        logger.info(f"Received text: {text}")
        return text

    def accept_alert(self, alert_window):
        logger.info("Accepting an alert")
        alert_window.accept()

    def deny_alert(self, alert_window):
        logger.info("Dismissing an alert")
        alert_window.dismiss()

    def alert_send_keys(self, alert_window, value):
        logger.info(f"Sending keys {value} in the alert {alert_window}")
        alert_window.send_keys(value)

    def is_alert_present(self):
        logger.info("Finding an alert presence")
        try:
            WebDriverWait(self.driver, self.TIMEOUT).until(expected_conditions.alert_is_present())
            logger.info("Found an alert")
            return True
        except:
            logger.info("Did not find an alert")
            return False
