import pyautogui
import Helpers.JAWSFSAPI as JF
from Helpers.imageToText import toText
from time import sleep


class ImageManager:
    def __init__(self, file_path="", description=""):
        self.file_path = file_path
        self.description = description

    def locate_center(self):
        resimVar = False
        resimSayac = 0
        while resimVar == False and resimSayac < 5:
            try:
                resimLoc = pyautogui.locateCenterOnScreen(
                    self.file_path, confidence=0.8
                )
                if not resimLoc is None:
                    resimVar = True
                JF.Speak("Düğme bulundu")
                sleep(1)
            except:
                JF.Speak("Düğme ekranda bulunamadı, tekrar aranacak")
                resimSayac = resimSayac + 1
                sleep(5)
        return resimLoc

        # locate the center of image

    def locate_topleft(self):
        return pyautogui.locateOnScreen(self.file_path, confidence=0.8)
        #  locate the position of image

    def click(self):
        resimloc = self.is_image_exist_on_window()
        if self.is_image_exist_on_window():
            print(self.file_path)
            pyautogui.click(resimloc)
            JF.Speak(f"{self.description} düğmesi tıklandı.")
            print(f"{self.description} düğmesi tıklandı.")
            print(self.file_path)
            return True
        else:
            print("Düğme bulunamadı.")
            JF.Speak(
                f"{self.description} düğmesi ekranda bulunamadı. Çıkış yapılıyor. Lütfen Tekrar deneyiniz."
            )
            return False

    def to_text(self):
        return toText(self.file_path)

    def text_to_speech(self):
        JF.Speak(self.to_text())
        pass

    def is_image_exist_on_window(self):
        location = self.locate_center()
        if location is not None:
            print(f"{self.description} - {self.file_path} bulundu")
            return location
        else:
            print(f"{self.description} - {self.file_path} bulunmadı")
            return False
