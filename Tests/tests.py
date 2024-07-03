import pytest
from Pages.main_page import MainPage
from Pages.search_page_for_the_request import SearchPageForTheRequest
from Configuration.test_utils import TestUtils

config = TestUtils.parse_config()


@pytest.mark.usefixtures("setup")
class TestSteam:
    URL = config['URL']

    @pytest.mark.parametrize(
        'search_word, range_num',
        [(param['search_word'], param['range_num']) for param in config['pytest_params']]
    )
    def test(self, setup, search_word, range_num):
        driver, web_pages = setup
        main_page = MainPage()
        main_page.driver = driver
        main_page.driver.get(self.URL)

        assert main_page.main_page_is_displayed(), 'The main page is not displayed'
        main_page.game_search(search_word)
        self.receiving_sorting_list(range_num)

    @staticmethod
    def receiving_sorting_list(range_num):
        search_page = SearchPageForTheRequest()
        assert search_page.search_page_is_displayed(), 'The search page is not displayed'
        search_page.sort_dropdown_menu()
        search_page.waiting_for_changing_price()

        prices_list = TestUtils.sorting_prices(search_page.get_price_texts(range_num), range_num)

        assert prices_list == sorted(prices_list, reverse=True), 'Price sorting is not working'
