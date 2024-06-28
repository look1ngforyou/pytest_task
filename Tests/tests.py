from selenium.webdriver.common.by import By
from Pages.MainPage import MainPage
from Pages.SearchPageForTheRequest import SearchPageForTheRequest
import pytest


class Tests:
    TITLE = ('Fallout', 'The Witcher')
    RANGE_NUM = (10, 20)

    @pytest.mark.parametrize(
        'main_steam_url, loaded_page_xpath, search_box_xpath, search_word, search_button_xpath',
        [
            ('https://store.steampowered.com/',
             (By.XPATH, '//div[contains(@class, "page_background_overlay")]'),
             (By.XPATH, '//*[@id="store_nav_search_term"]'),
             TITLE[0],
             (By.XPATH, '//*[@id="store_search_link"]//img'))
        ]
    )
    def test_main_page(self, main_steam_url, loaded_page_xpath, search_box_xpath, search_word, search_button_xpath):
        main_page = MainPage()
        main_page.setup(main_steam_url)

        assert main_page.main_page_is_displayed(loaded_page_xpath), 'The main page is not displayed'
        print('The main page is displayed')
        main_page.game_search(search_box_xpath, search_word, search_button_xpath)

    @pytest.mark.parametrize(
        'search_page_xpath_check, dropdown_xpath, selection_xpath, opacity_xpath, formatting_price, range_num',
        [
            ((By.XPATH, '//*[@id="search_result_container"]'),
             (By.XPATH, '//*[@id="sort_by_trigger"]'),
             (By.XPATH, '//*[@id="Price_DESC"]'),
             (By.XPATH, '//*[@id="search_result_container" and @style="opacity: 0.5;"]'),
             '(//div[contains(@class, "discount_final_price")])[{}]',
             RANGE_NUM[0])
        ]
    )
    def test_search_page(self, search_page_xpath_check, dropdown_xpath, selection_xpath, opacity_xpath,
                         formatting_price, range_num):
        search_page = SearchPageForTheRequest()
        next_page_url = MainPage.navigate_to_search_page()
        search_page.setup(next_page_url)

        assert search_page.search_page_is_displayed(search_page_xpath_check), 'The search page is not displayed'
        print('The search page is displayed')

        search_page.sort_dropdown_menu(dropdown_xpath, selection_xpath)

        search_page.waiting_for_changing_price(opacity_xpath)
        prices_list, sorted_prices = search_page.sorting_prices(formatting_price, range_num)

        assert prices_list == sorted_prices, "The prices list is not sorted from highest to lowest."
        print('The prices list sorted from highest to lowest')
        search_page.quit()  # Почему quit не работает я так и не понял)
