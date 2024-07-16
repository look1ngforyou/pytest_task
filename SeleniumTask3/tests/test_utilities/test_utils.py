import pyautogui as pyautogui
import time


def move_slider_to_aiming_value(slider_element, slider_locator, value_locator, aiming_value, max_value=5, min_value=0,
                                pixel_range=60, timeout=15):
    current_value = slider_element.get_slider_value(slider_locator)
    current_value = max(min(current_value, max_value), min_value)
    pixels_per_unit = pixel_range / (max_value - min_value)
    offset = (aiming_value - current_value) * pixels_per_unit

    if offset != 0:
        slider_element.move_slider(slider_locator, offset, timeout)
        final_value = slider_element.get_slider_value(slider_locator)
        aiming_value = max(min(aiming_value, max_value), min_value)
        assert final_value == aiming_value


def count_elements(driver, locator):
    elements = driver.find_elements(*locator)
    return len(elements)


def upload_file_via_fe(file_path):
    time.sleep(2)
    pyautogui.write(file_path)
    time.sleep(2)
    pyautogui.press('enter')
