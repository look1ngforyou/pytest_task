from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from Pages.WebPagesSingleton import WebPages


class MainPage:
    TIMEOUT = 15

    def __init__(self):
        web_pages = WebPages.get_instance()
        self.driver = web_pages.driver
        self.wait = WebDriverWait(self.driver, self.TIMEOUT)

    def setup(self, url):
        self.driver.get(url)

    def main_page_is_displayed(self, main_page_xpath_check):
        self.wait.until(ec.element_to_be_clickable(main_page_xpath_check))
        return True

    def game_search(self, search_box_xpath, search_word, search_button_xpath):
        search_box = self.wait.until(ec.presence_of_element_located(search_box_xpath))
        search_box.send_keys(search_word)
        self.wait.until(ec.element_to_be_clickable(search_button_xpath)).click()

    def quit(self):
        self.driver.quit()

    @staticmethod
    def navigate_to_search_page():
        return WebPages.get_instance().driver.current_url


