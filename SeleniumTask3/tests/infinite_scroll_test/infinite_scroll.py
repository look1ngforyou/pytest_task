import pytest
from selenium.webdriver.common.by import By
from tests.test_utilities.test_utils import count_elements
import logging

logging.basicConfig(
    filename='../test.log',
    level=logging.INFO,
    filemode="w",
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


@pytest.mark.usefixtures("setup")
class TestInfiniteScroll:
    def setup_method(self):
        inf_scroll_data = self.test_data["infinite_scroll"]
        self.url = inf_scroll_data["URL"]
        self.paragraph = (By.XPATH, '//div[contains(@class, "jscroll-added")]')
        self.number = inf_scroll_data["target_number"]
        self.unique_element = (By.XPATH, '//div[contains(@class, "example")]')

    def test_inf_scroll(self):
        self.browser.get_url(self.url)
        assert self.label_element.presence_located(self.unique_element), 'Failed to open the main page'
        logging.warning("Successfully opened the main page")

        while True:
            self.browser.scroll_to_defined_value(1000)
            paragraph_count = count_elements(self.browser.driver, self.paragraph)
            if paragraph_count >= self.number:
                break

        assert paragraph_count >= self.number, "The expected number of paragraphs was not found."
        logging.warning("The expected number of paragraphs was found.")
