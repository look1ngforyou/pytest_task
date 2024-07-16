from selenium.webdriver import Chrome, Firefox, Edge


class BrowserFactory:
    @staticmethod
    def get_driver(browser_type):
        driver = None
        if browser_type.lower() == "chrome":
            driver = Chrome()
        elif browser_type.lower() == "firefox":
            driver = Firefox()
        elif browser_type.lower() == "edge":
            driver = Edge()
        return driver
