import logging
from web_pages.handlers_page import Page1


class TestHandlers:
    URL = "https://the-internet.herokuapp.com/windows"
    NEW_WINDOW_TITLE = "New Window"
    MAIN_PAGE_TITLE = "The Internet"

    def test(self, browser):
        logger = logging.getLogger('logger')
        logger.info("Executing handlers test")
        self.page_1 = Page1(browser)

        browser.get(self.URL)
        self.page_1.wait_for_open()

        main_window = browser.current_window_handle()

        self.page_1.click()
        browser.switch_to_new_tab(main_window)

        title = browser.title()
        assert title == self.NEW_WINDOW_TITLE, f"Failed to open {self.NEW_WINDOW_TITLE} page"

        browser.switch_to_window(main_window)
        self.page_1.wait_for_open()

        self.page_1.click()
        browser.switch_to_new_tab(main_window)

        title = browser.title()
        assert title == self.NEW_WINDOW_TITLE, f"Failed to open {self.NEW_WINDOW_TITLE} page"

        browser.switch_to_window(main_window)
        self.page_1.wait_for_open()

        browser.close_tab_by_title(self.NEW_WINDOW_TITLE)
        browser.close_tab_by_title(self.NEW_WINDOW_TITLE)