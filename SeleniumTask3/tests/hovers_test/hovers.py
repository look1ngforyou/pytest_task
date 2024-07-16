import pytest
from selenium.webdriver.common.by import By
import logging

logging.basicConfig(
    filename='../test.log',
    level=logging.INFO,
    filemode="w",
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

@pytest.mark.usefixtures("setup")
class TestHovers:
    def setup_method(self):
        hover_data = self.test_data["hovers"]
        self.url = hover_data["URL"]
        self.unique_element = (By.XPATH, '//div[contains(@class, "example")]')
        self.url_check_template = '/users/{}'
        self.figure_template = '(//div[contains(@class,"figure")])[{}]'
        self.caption_template = '(//div[contains(@class,"figcaption")])[{}]/h5'
        self.view_profile_template = '(//div[contains(@class,"figcaption")])[{}]//a'
        self.usernames = {
            1: 'name: user1',
            2: 'name: user2',
            3: 'name: user3'
        }

    def hover(self, index):
        figure_locator = (By.XPATH, self.figure_template.format(index))
        caption_locator = (By.XPATH, self.caption_template.format(index))
        username = self.usernames[index]
        view_profile_locator = (By.XPATH, self.view_profile_template.format(index))

        self.browser.get_url(self.url)
        assert self.label_element.presence_located(self.unique_element), 'Failed to open the main page'
        logging.warning("Successfully opened the main page")

        self.slider_element.hover_over_element(figure_locator)
        assert self.web_element.get_text(caption_locator) == username, 'Correct username is not displayed'
        logging.warning('Correct username is displayed')

        self.web_element.click_on_element(view_profile_locator)
        assert self.browser.get_current_url().endswith(
            self.url_check_template.format(index)), 'The link did not open for the suggested user'
        logging.warning('The link correctly displaying for suggested user')
        self.browser.back_to_previous_url()
        assert self.browser.get_current_url() == self.url, 'The main page is not displayed'
        logging.warning('The main page is displayed')

    def test_hovers_1(self):
        self.hover(1)

    def test_hovers_2(self):
        self.hover(2)

    def test_hovers_3(self):
        self.hover(3)
