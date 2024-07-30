from selenium.webdriver import Chrome, Firefox, Edge
import logging

logger = logging.getLogger('logger')


class BrowserFactory:
    @staticmethod
    def get_driver(browser_type):
        if browser_type.lower() == "chrome":
            driver = Chrome()
        elif browser_type.lower() == "firefox":
            driver = Firefox()
        elif browser_type.lower() == "edge":
            driver = Edge()
        else:
            raise ValueError(f"Do not support this browser type {browser_type}")
        logger.info(f"Returning the browser type {browser_type} from the BrowserFactory")
        return driver
