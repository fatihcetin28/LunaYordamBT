import pyautogui

def image_location_center(file_path):
    return pyautogui.locateCenterOnScreen(file_path, confidence=0.9)

def image_location_position(file_path):
    return pyautogui.locateOnScreen(file_path, confidence=0.9)