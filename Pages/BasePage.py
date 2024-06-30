from selenium.webdriver.support.ui import WebDriverWait
from Pages.WebPagesSingleton import WebPages


class BasePage:
    TIMEOUT = 15

    def __init__(self):
        web_pages = WebPages.get_instance()
        self.driver = web_pages.driver
        self.wait = WebDriverWait(self.driver, self.TIMEOUT)
