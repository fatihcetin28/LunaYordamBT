import DetectImageLocation as dti
import pyautogui
import JAWSFSAPI as JF
from imageToText import toText

class ImageManager:
    def __init__(self, file_path="", description=""):
        self.file_path = file_path
        self.description = description

    def locate_center(self):
       return dti.image_location_center(self.file_path)
        # locate the center of image

    def locate_topleft(self):
        return dti.image_location_position(self.file_path)
        #  locate the position of image

    def click(self):
        if self.is_image_exist_on_window():
            pyautogui.click(self.file_path)
            JF.Speak(f"{self.description} düğmesi tıklandı.")
        else:
            print("Button not found on the window.")
            JF.Speak(f"{self.description} düğmesi ekranda bulunamadı. Çıkış yapılıyor. Lütfen Tekrar deneyiniz.")
    
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
