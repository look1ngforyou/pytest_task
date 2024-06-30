import pytest
from selenium import webdriver
from Pages.WebPagesSingleton import WebPages


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    WebPages._instance = None
    web_pages = WebPages()
    web_pages.driver = driver

    request.cls.driver = driver
    yield
    driver.quit()
