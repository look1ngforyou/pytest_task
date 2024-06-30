from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from Pages.BasePage import BasePage
from Configuration.TestUtils import sorting_prices


class SearchPageForTheRequest(BasePage):
    SEARCH_PAGE_ID_CHECK = (By.ID, 'search_result_container')
    DROPDOWN_ID = (By.ID, 'sort_by_trigger')
    SELECTION_ID = (By.ID, 'Price_DESC')
    OPACITY_XPATH = (By.XPATH, '//*[@id="search_result_container" and @style="opacity: 0.5;"]')
    FORMATTING_PRICE_TEMPLATE = '(//div[contains(@class, "discount_final_price")])[{}]'

    def search_page_is_displayed(self):
        if self.wait.until(ec.presence_of_element_located(self.SEARCH_PAGE_ID_CHECK)):
            return True

    def sort_dropdown_menu(self):
        self.wait.until(ec.element_to_be_clickable(self.DROPDOWN_ID)).click()
        self.wait.until(ec.element_to_be_clickable(self.SELECTION_ID)).click()

    def waiting_for_changing_price(self):
        try:
            self.wait.until(ec.presence_of_element_located(self.OPACITY_XPATH))
        except TimeoutException:
            pass

    def sorting_prices(self, range_num):
        return sorting_prices(self.driver, self.wait, range_num, self.FORMATTING_PRICE_TEMPLATE)
