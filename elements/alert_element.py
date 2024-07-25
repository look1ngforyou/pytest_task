from elements.base_element import BaseElement
import logging


class AlertElement(BaseElement):
    def __init__(self, driver, locator_1=None, attribute=None, timeout=15):
        super().__init__(driver, locator_1 or (None, None), attribute, timeout)

    def alert_text(self, alert_window):
        logging.info("Getting an alert text")
        text = alert_window.text
        logging.info(f"Received text: {text}")
        return text

    def accept_alert(self, alert_window):
        logging.info("Accepting an alert")
        alert_window.accept()
        logging.info("Accepted an alert")

    def deny_alert(self, alert_window):
        logging.info("Dismissing an alert")
        alert_window.dismiss()
        logging.info("Dismissed an alert")

    def alert_send_keys(self, alert_window, value):
        logging.info("Sending keys in the alert")
        alert_window.send_keys(value)
        logging.info("Sent keys in the alert")

    def presence_of_alert(self):
        logging.info("Finding an alert presence")
        try:
            self.wait(self.driver, 5).until(self.ec.alert_is_present())
            logging.info("Found an alert")
            return True
        except:
            logging.info("Did not find an alert")
            return False
