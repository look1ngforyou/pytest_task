from selenium.webdriver.support.ui import WebDriverWait
from Pages.driver_singleton import WebPages
from Configuration.test_utils import TestUtils

config = TestUtils.parse_config()


class BasePage:
    TIMEOUT = config["TIMEOUT"]

    def __init__(self):
        web_pages = WebPages.get_instance()
        self.driver = web_pages.driver
        self.wait = WebDriverWait(self.driver, self.TIMEOUT)
