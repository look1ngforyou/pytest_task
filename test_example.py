from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from faker import Faker


class TestWebsite:
    TIMEOUT = 5
    URL = "https://store.steampowered.com/"

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.driver = Chrome()
        self.wait = WebDriverWait(self.driver, self.TIMEOUT)
        yield
        self.driver.quit()

    @pytest.mark.parametrize("url, body_xpath, main_page_xpath, username_xpath, password_xpath, error_xpath",
                             [(URL, (By.XPATH, '//body'),
                               (By.XPATH, '//a[contains(@class, "global_action_link")]'),
                               (By.XPATH, '(//input[contains(@type, "text")])[1]'),
                               (By.XPATH, '//input[contains(@type, "password")]'),
                               (By.XPATH, "//div[contains(text(), 'Пожалуйста, проверьте')]"))])
    def test_combined_function(self, url, body_xpath, main_page_xpath, username_xpath, password_xpath, error_xpath):
        self.driver.get(url)
        fake = Faker()
        try:
            page_displaying = self.wait.until(ec.presence_of_element_located(body_xpath))
            assert page_displaying is not None
            print(' The main page is displayed.')

            login_page_button_transmission = self.wait.until(ec.element_to_be_clickable(main_page_xpath))
            login_page_button_transmission.click()
            assert self.driver.current_url[:37] == 'https://store.steampowered.com/login/'
            print('The login page is opened.')

            username_input = self.wait.until(ec.element_to_be_clickable(username_xpath))
            password_input = self.wait.until(ec.element_to_be_clickable(password_xpath))

            username_input.send_keys(fake.email())
            password_input.send_keys(fake.password())

            login_button = self.wait.until(ec.element_to_be_clickable(
                (By.XPATH, '//button[contains(@type, "submit")]')))
            login_button.click()
            unsuccessful_login = self.wait.until(ec.presence_of_element_located(error_xpath))
            assert unsuccessful_login is not None
            print('The error text is displayed.')
        except Exception:
            pytest.fail()


if __name__ == "__main__":
    TestWebsite()
