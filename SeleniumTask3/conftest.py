import pytest
import json
import os
from browser_setting.browser import Browser
from base_element_and_descendants.web_element import WebElement
from base_element_and_descendants.slider_element import SliderElement
from base_element_and_descendants.alert_element import AlertElement
from base_element_and_descendants.button_element import ButtonElement
from base_element_and_descendants.label_element import LabelElement
from base_element_and_descendants.iframe_element import IframeElement
from base_element_and_descendants.input_element import InputElement


@pytest.fixture(scope="session")
def test_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'test_data.json')

    with open(file_path, 'r') as file:
        return json.load(file)


@pytest.fixture(scope="class")
def setup(request, test_data):
    browser = Browser("chrome")
    driver = browser.driver

    request.cls.browser = browser
    request.cls.test_data = test_data

    request.cls.button_element = ButtonElement(driver)
    request.cls.alert_element = AlertElement(driver)
    request.cls.web_element = WebElement(driver)
    request.cls.slider_element = SliderElement(driver)
    request.cls.label_element = LabelElement(driver)
    request.cls.iframe_element = IframeElement(driver)
    request.cls.input_element = InputElement(driver)

    yield

    driver.quit()
