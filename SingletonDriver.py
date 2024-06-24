from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class SingletonDriver:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonDriver, cls).__new__(cls)
            cls._instance.driver = Chrome()
        return cls._instance

    def quit_driver(self):
        return self.driver.quit()


a = SingletonDriver()
b = SingletonDriver()
print(a is b)
if __name__ == '__main__':
    SingletonDriver()
