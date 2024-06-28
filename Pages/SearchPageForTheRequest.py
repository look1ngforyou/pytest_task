from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from Pages.WebPagesSingleton import WebPages


class SearchPageForTheRequest:
    TIMEOUT = 15

    def __init__(self):
        web_pages = WebPages.get_instance()
        self.driver = web_pages.driver
        self.wait = WebDriverWait(self.driver, self.TIMEOUT)

    def setup(self, url):
        self.driver.get(url)

    def search_page_is_displayed(self, search_page_xpath_check):
        if self.wait.until(ec.presence_of_element_located(search_page_xpath_check)):
            return True

    def sort_dropdown_menu(self, dropdown_xpath, selection_xpath):
        self.wait.until(ec.element_to_be_clickable(dropdown_xpath)).click()
        self.wait.until(ec.element_to_be_clickable(selection_xpath)).click()

    def waiting_for_changing_price(self, opacity_xpath):
        try:
            self.wait.until(ec.presence_of_element_located(opacity_xpath))
        except TimeoutException:
            pass

    def quit(self):
        self.driver.quit()

    def sorting_prices(self, formatting_price_xpath, range_num):
        prices_list = []
        for i in range(1, range_num + 1):
            dynamic_xpath = formatting_price_xpath.format(i)
            dynamic_price_xpath = (By.XPATH, dynamic_xpath)

            try:
                game_price_element = self.wait.until(ec.visibility_of_element_located(dynamic_price_xpath))
                price_text = game_price_element.text.strip()

                if price_text.lower() in ['free to play', 'free', 'бесплатно']:
                    continue

                if price_text.lower().startswith('your price:') or price_text.lower().startswith('цена для вас:'):
                    price_text = price_text.split(':', 1)[-1].strip()

                price = price_text[:-1].replace(',', '.')
                final_price = float(price)
                prices_list.append(final_price)

            except TimeoutException:
                continue

        sorted_prices = sorted(prices_list, reverse=True)
        return prices_list, sorted_prices
