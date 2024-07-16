from selenium.webdriver.support.wait import WebDriverWait
from base_element_and_descendants.base_element import BaseElement
from selenium.webdriver.support import expected_conditions as ec
import logging


class IframeElement(BaseElement):
    def get_text_from_iframe(self, iframe_locator, element_locator_inside_iframe, timeout=15):
        logging.info(f"Switching to iframe with locator: {iframe_locator}")
        iframe = WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(iframe_locator))
        self.driver.switch_to.frame(iframe)
        logging.info("Successfully switched to iframe")

        logging.info(f"Waiting for element inside iframe with locator: {element_locator_inside_iframe}")
        element_inside_iframe = WebDriverWait(self.driver, timeout).until(
            ec.presence_of_element_located(element_locator_inside_iframe))
        text = element_inside_iframe.text

        logging.info(f"Returning text from iframe: {text}")

        logging.info("Switching back to default content")
        self.driver.switch_to.default_content()
        logging.info("Successfully switched to default content")

        return text

    def get_text_from_nested_iframe(self, parent_iframe_locator, child_iframe_locator,
                                    element_locator_inside_iframe,
                                    timeout=15):
        logging.info(f"Switching to parent iframe with locator: {parent_iframe_locator}")
        parent_iframe = WebDriverWait(self.driver, timeout).until(
            ec.presence_of_element_located(parent_iframe_locator))
        self.driver.switch_to.frame(parent_iframe)
        logging.info("Successfully switched to parent iframe")

        logging.info(f"Switching to child iframe with locator: {child_iframe_locator}")
        child_iframe = WebDriverWait(self.driver, timeout).until(
            ec.presence_of_element_located(child_iframe_locator))
        self.driver.switch_to.frame(child_iframe)
        logging.info("Successfully switched to child iframe")

        logging.info(f"Waiting for element inside child iframe with locator: {element_locator_inside_iframe}")
        element_inside_iframe = WebDriverWait(self.driver, timeout).until(
            ec.presence_of_element_located(element_locator_inside_iframe))
        text = element_inside_iframe.text

        logging.info(f"Returning text from nested iframe: {text}")

        logging.info("Switching back to parent iframe")
        self.driver.switch_to.parent_frame()
        logging.info("Successfully switched back to parent iframe")

        logging.info("Switching back to default content")
        self.driver.switch_to.default_content()
        logging.info("Successfully switched to default content")

        return text

