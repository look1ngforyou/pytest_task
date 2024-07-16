from selenium.webdriver.support.wait import WebDriverWait
from base_element_and_descendants.base_element import BaseElement
from selenium.webdriver.support import expected_conditions as ec
import logging


class AlertElement(BaseElement):
    def alert_text(self):
        logging.info("Trying to get an alert text")
        logging.info("Switching to an alert")
        alert_window = self.driver.switch_to.alert
        logging.info("Successfully switched to an alert")
        logging.info("Getting text")
        text = alert_window.text
        logging.info(f"Successfully received text: {text}")
        return text

    def accept_alert(self):
        logging.info("Trying to accept an alert")
        logging.info("Switching to an alert")
        alert_window = self.driver.switch_to.alert
        logging.info("Successfully switched to an alert")
        logging.info("Accepting an alert")
        alert_window.accept()
        logging.info("Successfully accepted an alert")

    def deny_alert(self):
        logging.info("Trying to dismiss an alert")
        logging.info("Switching to an alert")
        alert_window = self.driver.switch_to.alert
        logging.info("Successfully switched to an alert")
        logging.info("Trying to dismiss an alert")
        alert_window.dismiss()
        logging.info("Successfully dismissed an alert")

    def presence_of_alert(self):
        logging.info("Trying to find an alert presence")
        try:
            WebDriverWait(self.driver, 5).until(ec.alert_is_present())
            logging.info("Found an alert")
            return True
        except:
            logging.info("Did not find an alert")
            return False
