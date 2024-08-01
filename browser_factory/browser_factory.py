from selenium.webdriver import Chrome, Firefox, Edge
from selenium.webdriver import ChromeOptions
import logging

logger = logging.getLogger('logger')


class BrowserFactory:
    @staticmethod
    def get_driver(browser_type, arguments):
        if browser_type.lower() == "chrome":
            options = ChromeOptions()
            options.add_argument(argument=arguments)
            driver = Chrome(options=options)
        elif browser_type.lower() == "firefox":
            driver = Firefox()
        elif browser_type.lower() == "edge":
            driver = Edge()
        else:
            raise ValueError(f"Do not support this browser type {browser_type}")
        logger.info(f"Returning the browser type {browser_type} from the BrowserFactory")
        return driver
