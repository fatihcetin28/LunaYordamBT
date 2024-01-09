from Helpers.JAWSFSAPI import Speak
from Helpers.JAWSFSAPI import StartSpeech
import pyautogui
import time
from Helpers.imageToText import toText
from Helpers.window_max_min import minimize_window
from os import remove
import Data.Strings as Strings
import Data.Speechs as Speechs
import Helpers.handleScreenshot as SS


def handleUyariOdunc():
    window_title = Strings.yordam_title

    uyariVarMi = pyautogui.locateCenterOnScreen(
        Strings.uyariBaslikImage, confidence=0.9
    )

    if uyariVarMi is not None:
        SS.takeSS()

        Speak(Speechs.uyariVerdi)
        im = pyautogui.screenshot(region=(500, 320, 345, 175))
        im.save(Strings.uyariSaveFilePath)

        time.sleep(0.5)

        text = toText(Strings.uyariSaveFilePath)

        time.sleep(0.5)

        Speak(text)

        print(text)

        time.sleep(3)

        Speak(Speechs.uyari_islemden_cikis)

        time.sleep(0.5)

        pyautogui.press("enter")

        time.sleep(0.5)

        minimize_window(window_title)

        remove(Strings.uyariSaveFilePath)

        StartSpeech()

        exit()
    else:
        SS.takeSS()
        Speak(Speechs.tc_demirbas_gecerli)
