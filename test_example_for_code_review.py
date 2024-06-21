from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from faker import Faker


class TestWebsite:
    TIMEOUT = 15
    URL = "https://store.steampowered.com/"

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.driver = Chrome()
        yield self.driver
        self.driver.quit()

    @pytest.mark.parametrize(
        "url, body_xpath, main_page_xpath, login_page_xpath, username_xpath, password_xpath, login_xpath, error_xpath",
        [(URL, (By.XPATH, '//a[contains(@class, "promo_link")]'),
          (By.XPATH, '//a[contains(@class, "global_action_link")]'),
          (By.XPATH, '//div[contains(@style, "grid-template-columns: repeat(41, 1fr);")]'),
          (By.XPATH, '(//input[contains(@type, "text")])[1]'),
          (By.XPATH, '//input[contains(@type, "password")]'),
          (By.XPATH, '//button[contains(@type, "submit")]'),
          (By.XPATH, "//div[contains(text(), 'Пожалуйста, проверьте')]"))])
    def test_combined_function(self, url, body_xpath, main_page_xpath, login_page_xpath, username_xpath, password_xpath,
                               login_xpath, error_xpath):
        self.driver.get(url)
        wait = WebDriverWait(self.driver, timeout=self.TIMEOUT)
        fake = Faker()

        page_displaying = wait.until(ec.presence_of_element_located(body_xpath))
        assert page_displaying is not None
        print('The main page is displayed.')

        login_page_button_transmission = wait.until(ec.element_to_be_clickable(main_page_xpath))
        login_page_button_transmission.click()

        assert wait.until(ec.visibility_of_element_located(login_page_xpath))
        print('The login page is opened.')

        username_input = wait.until(ec.element_to_be_clickable(username_xpath))
        password_input = wait.until(ec.element_to_be_clickable(password_xpath))

        username_input.send_keys(fake.email())
        password_input.send_keys(fake.password())

        login_button = wait.until(ec.element_to_be_clickable(login_xpath))
        login_button.click()

        unsuccessful_login = wait.until(ec.presence_of_element_located(error_xpath))
        assert unsuccessful_login is not None
        print('The error text is displayed.')
