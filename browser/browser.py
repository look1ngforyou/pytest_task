from browser_factory.browser_factory import BrowserFactory
import logging


class Browser:
    def __init__(self, browser_type):
        logging.info(f"Initializing the browser with type: {browser_type}")
        self.driver = BrowserFactory.get_driver(browser_type)
        logging.info(f"Initialized the browser")

    def get(self, url):
        logging.info(f"Navigating to the URL with address: {url}")
        self.driver.get(url)
        logging.info(f"Navigated to the suggested URL")

    def quit(self):
        logging.info("Closing the browser")
        self.driver.quit()
        logging.info("Closed the browser")

    def current_url(self):
        logging.info("Getting the current URL address")
        current_url = self.driver.current_url
        logging.info(f"Current URl is {current_url}")
        logging.info("Returning the current URL")
        return current_url

    def back(self):
        logging.info("Navigating to the previous URL")
        self.driver.back()
        logging.info("Navigated back to the previous URL")

    def title(self):
        logging.info("Getting the page title")
        title = self.driver.title
        logging.info(f"The page title is {title}")
        logging.info(f"Returning the page title")
        return title

    def close(self):
        logging.info("Closing the current page")
        self.driver.close()
        logging.info("Closed the current page")

    def refresh(self):
        logging.info("Refreshing thr current page")
        self.driver.refresh()
        logging.info("Refreshed the current page")

    def execute_script(self, script, *args):
        logging.info("Executing JavaScript")
        result = self.driver.execute_script(script, *args)
        logging.info(f"Executed script {script} with the arguments {args}")
        return result

    def current_window_handle(self):
        logging.info("Getting current window handle")
        current_handle = self.driver.current_window_handle
        logging.info("Got current window handle")
        return current_handle

    def switch_to_new_tab(self, current_window_handle):
        logging.info("Switching to the new tab with handle")
        new_window_handle = None
        for handle in self.driver.window_handles:
            if handle != current_window_handle:
                new_window_handle = handle
                break
        self.driver.switch_to.window(new_window_handle)
        logging.info(f"Switched to the new tab with handle: {new_window_handle}")
        return new_window_handle

    def switch_to_iframe(self, iframe_loc):
        logging.info("Switching to an iframe")
        self.driver.switch_to.frame(iframe_loc)
        logging.info("Switched to an iframe")

    def switch_to_window(self, window_handle):
        logging.info(f"Switching to the window with handle: {window_handle}")
        self.driver.switch_to.window(window_handle)
        logging.info("Switched to the window")

    def switch_to_alert(self):
        logging.info("Switching to an alert")
        alert = self.driver.switch_to.alert
        logging.info("Switched to an alert")
        return alert

    def close_tab_by_title(self, title):
        logging.info(f"Closing the tab with the title: {title}")
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.title() == title:
                self.close()
                logging.info(f"Closed the tab with the title {title}")
                break

    def __getattr__(self, item):
        return getattr(self.driver, item)
