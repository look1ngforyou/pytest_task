import pyautogui as pyautogui
import time


def upload_file_via_fe(file_path):
    time.sleep(1)
    pyautogui.write(file_path)
    time.sleep(1)
    pyautogui.press('enter')