from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from Pages.base_page import BasePage


class SearchPageForTheRequest(BasePage):
    SEARCH_PAGE_ID_CHECK = (By.ID, 'search_result_container')
    DROPDOWN_ID = (By.ID, 'sort_by_trigger')
    SELECTION_ID = (By.ID, 'Price_DESC')
    OPACITY_XPATH = (By.XPATH, '//*[@id="search_result_container" and @style="opacity: 0.5;"]')
    FORMATTING_PRICE_TEMPLATE = '(//div[contains(@class, "discount_final_price")])[{}]'

    def search_page_is_displayed(self):
        return bool(self.wait.until(ec.presence_of_element_located(self.SEARCH_PAGE_ID_CHECK)))

    def sort_dropdown_menu(self):
        self.wait.until(ec.element_to_be_clickable(self.DROPDOWN_ID)).click()
        self.wait.until(ec.element_to_be_clickable(self.SELECTION_ID)).click()

    def waiting_for_changing_price(self):
        """
            Нужно обработать исключение, так как элемент "затененности","затухания","прогрузки" находится селениумом
            через раз,как я понял селениум делает запросы каждые 0.5 секунд, а элемент появляется на 0.4-0.5 секунды,
            следовательно он может не попасть в это окно и он уже никогда не будет найден и мы поймаем ошибку.
        """
        try:
            self.wait.until(ec.presence_of_element_located(self.OPACITY_XPATH))
        except TimeoutException:
            pass

    def get_price_texts(self, range_num):
        price_texts = []
        for i in range(1, range_num + 1):
            dynamic_xpath = self.FORMATTING_PRICE_TEMPLATE.format(i)
            dynamic_price_xpath = (By.XPATH, dynamic_xpath)

            game_price_element = self.wait.until(ec.visibility_of_element_located(dynamic_price_xpath))
            price_texts.append(game_price_element.text)

        return price_texts
