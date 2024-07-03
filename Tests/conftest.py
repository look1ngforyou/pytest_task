import pytest
from selenium import webdriver
from Pages.driver_singleton import WebPages


@pytest.fixture(scope="class")
def setup():
    driver = webdriver.Chrome()
    WebPages._instance = None
    web_pages = WebPages()
    web_pages.driver = driver

    yield driver, web_pages

    driver.quit()
