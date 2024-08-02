import logging
from web_pages.handlers_page import Page1
from config import config


class TestHandlers:
    EXPECTED_NEW_WINDOW_TITLE = "New Window"

    def test_handlers(self, browser):
        logger = logging.getLogger('logger')
        logger.info("Execute handlers test")
        browser.get(config.HANDLERS_URL)

        self.HandlersPage = Page1(browser)
        self.HandlersPage.wait_for_open()

        main_window = browser.get_current_window_handle()

        self.HandlersPage.click_for_new_tab()

        browser.switch_to_the_tab(main_window)

        actual_title = browser.get_title()

        assert actual_title == self.EXPECTED_NEW_WINDOW_TITLE, \
            f"Failed to open {self.EXPECTED_NEW_WINDOW_TITLE} page"

        browser.switch_to_window(main_window)
        self.HandlersPage.wait_for_open()

        self.HandlersPage.click_for_new_tab()
        browser.switch_to_the_tab(main_window)

        actual_title = browser.get_title()
        assert actual_title == self.EXPECTED_NEW_WINDOW_TITLE, \
            f"Failed to open {self.EXPECTED_NEW_WINDOW_TITLE} page"

        browser.switch_to_window(main_window)
        self.HandlersPage.wait_for_open()

        browser.close_tab_by_title(self.EXPECTED_NEW_WINDOW_TITLE)
        browser.close_tab_by_title(self.EXPECTED_NEW_WINDOW_TITLE)
