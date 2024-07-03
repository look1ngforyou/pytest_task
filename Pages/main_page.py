from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from Pages.base_page import BasePage


class MainPage(BasePage):
    LOADED_PAGE_XPATH = (By.XPATH, '//div[contains(@class, "page_background_overlay")]')
    SEARCH_BOX_ID = (By.ID, 'store_nav_search_term')
    SEARCH_BUTTON_XPATH = (By.XPATH, '//*[@id="store_search_link"]//img')

    def main_page_is_displayed(self):
        return bool(self.wait.until(ec.element_to_be_clickable(self.LOADED_PAGE_XPATH)))

    def game_search(self, search_word):
        search_box = self.wait.until(ec.presence_of_element_located(self.SEARCH_BOX_ID))
        search_box.send_keys(search_word)
        self.wait.until(ec.element_to_be_clickable(self.SEARCH_BUTTON_XPATH)).click()
