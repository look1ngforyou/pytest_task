import pyautogui as pyautogui
import time


def upload_file_via_fe(file_path):
    time.sleep(2)
    pyautogui.write(file_path)
    time.sleep(2)
    pyautogui.press('enter')