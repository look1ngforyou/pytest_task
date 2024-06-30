import pytest
from Pages.MainPage import MainPage
from Pages.SearchPageForTheRequest import SearchPageForTheRequest


@pytest.mark.usefixtures("setup")
class TestSteam:
    URL = 'https://store.steampowered.com/'

    @pytest.mark.parametrize(
        'main_steam_url, search_word, range_num',
        [
            (URL, 'Fallout', 10),
            (URL, 'The Witcher', 20)
        ]
    )
    def test(self, main_steam_url, search_word, range_num):
        main_page = MainPage()
        main_page.driver.get(main_steam_url)

        assert main_page.main_page_is_displayed()
        main_page.game_search(search_word)

        self.receiving_sorting_prices(range_num)

    @staticmethod
    def receiving_sorting_prices(range_num):
        search_page = SearchPageForTheRequest()

        assert search_page.search_page_is_displayed()

        search_page.sort_dropdown_menu()
        search_page.waiting_for_changing_price()

        prices_list = search_page.sorting_prices(range_num)

        assert prices_list == sorted(prices_list, reverse=True)
