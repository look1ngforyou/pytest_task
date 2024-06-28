from selenium.webdriver import Chrome


class WebPages:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WebPages, cls).__new__(cls)
            cls._instance.driver = Chrome()
        return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def quit_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
