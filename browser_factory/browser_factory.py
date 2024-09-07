from selenium.webdriver import Chrome, Firefox, Edge
from selenium.webdriver import ChromeOptions
import logging

logger = logging.getLogger('logger')


class BrowserFactory:
    CHROME = "chrome"
    FIREFOX = "firefox"
    EDGE = "edge"
    DEFAULT_BROWSER = CHROME
    AVAILABLE_BROWSERS = [CHROME, FIREFOX, EDGE]

    @staticmethod
    def get_driver(browser_type=DEFAULT_BROWSER, arguments=None, headless=False):
        if browser_type.lower() == BrowserFactory.CHROME:
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless")
            if arguments:
                for argument in arguments:
                    options.add_argument(argument)
            driver = Chrome(options=options)
        elif browser_type.lower() == BrowserFactory.FIREFOX:
            driver = Firefox()
        elif browser_type.lower() == BrowserFactory.EDGE:
            driver = Edge()
        else:
            raise ValueError(f"Do not support this browser type {browser_type}")
        logger.info(f"Return the browser type {browser_type} from the BrowserFactory")
        return driver
