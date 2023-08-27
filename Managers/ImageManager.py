import pyautogui
import Helpers.JAWSFSAPI as JF
from Helpers.imageToText import toText

class ImageManager:
    def __init__(self, file_path="", description=""):
        self.file_path = file_path
        self.description = description

    def locate_center(self):
       return pyautogui.locateCenterOnScreen(self.file_path, confidence=0.9)
        # locate the center of image

    def locate_topleft(self):
        return pyautogui.locateOnScreen(self.file_path, confidence=0.9)
        #  locate the position of image

    def click(self):
        if self.is_image_exist_on_window():
            pyautogui.click(self.file_path)
            JF.Speak(f"{self.description} düğmesi tıklandı.")
            return True
        else:
            print("Düğme bulunamadı.")
            JF.Speak(f"{self.description} düğmesi ekranda bulunamadı. Çıkış yapılıyor. Lütfen Tekrar deneyiniz.")
            return False
    
    def to_text(self):
        return toText(self.file_path)

    def text_to_speech(self):
        JF.Speak(self.to_text())
        pass

    def is_image_exist_on_window(self):
        if self.locate_center() is not None:
            return True
        else:
            return False
