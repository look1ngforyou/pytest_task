import logging
from web_pages.handlers_page import Page1
from config import config


class TestHandlers:
    URL = config.HANDLERS_URL
    NEW_WINDOW_TITLE = "New Window"
    MAIN_PAGE_TITLE = "The Internet"

    def test_handlers(self, browser):
        logger = logging.getLogger('logger')
        logger.info("Executing handlers test")
        browser.get(self.URL)

        self.page_1 = Page1(browser)
        self.page_1.wait_for_open()

        main_window = browser.get_current_window_handle()

        self.page_1.click_for_new_tab()

        browser.switch_to_the_tab(main_window)

        title = browser.get_title()

        assert title == self.NEW_WINDOW_TITLE, f"Failed to open {self.NEW_WINDOW_TITLE} page"

        browser.switch_to_window(main_window)
        self.page_1.wait_for_open()

        self.page_1.click_for_new_tab()
        browser.switch_to_the_tab(main_window)

        title = browser.get_title()
        assert title == self.NEW_WINDOW_TITLE, f"Failed to open {self.NEW_WINDOW_TITLE} page"

        browser.switch_to_window(main_window)
        self.page_1.wait_for_open()

        browser.close_tab_by_title(self.NEW_WINDOW_TITLE)
        browser.close_tab_by_title(self.NEW_WINDOW_TITLE)