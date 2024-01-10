import pyautogui
import Helpers.JAWSFSAPI as JF
from Helpers.imageToText import toText
from time import sleep
from Helpers.loggers import ImageClickLogger

logger = ImageClickLogger()


class ImageManager:
    def __init__(self, file_path="", description=""):
        self.file_path = file_path
        self.description = description

    def locate_center(self):
        resimVar = False
        resimSayac = 0
        while resimVar == False and resimSayac < 5:
            resimLoc = pyautogui.locateCenterOnScreen(self.file_path, confidence=0.8)
            if resimLoc is not None:
                resimVar = True
                JF.Speak(f"{self.description} düğmesi {resimSayac+1}. denemede bulundu")
                sleep(1)
                logger.debug(
                    f"{self.description} düğmesi {resimSayac+1}. denemede bulundu"
                )
            else:
                JF.Speak(
                    f"{self.description} düğmesi {resimSayac+1}. denemede ekranda bulunamadı, tekrar aranacak"
                )
                logger.debug(
                    f"{self.description} düğmesi {resimSayac+1}. denemede ekranda bulunamadı, tekrar aranacak"
                )
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
            pyautogui.click(resimloc)
            JF.Speak(f"{self.description} düğmesi tıklandı.")
            logger.debug(f"{self.description} düğmesi tıklandı.")
            logger.debug(self.file_path)
            return True
        else:
            logger.debug(f"{self.description} düğmesi bulunamadı.")
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
            logger.debug(f"{self.description} - {self.file_path} bulundu")
            return location
        else:
            logger.debug(f"{self.description} - {self.file_path} bulunmadı")
            return False
