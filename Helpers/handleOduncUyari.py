from Helpers.JAWSFSAPI import Speak
import pyautogui
import time
from Helpers.imageToText import toText
from Helpers.window_max_min import minimize_window
from os import remove
import Data.Strings as Strings
import Data.Speechs as Speechs


def handleUyariOdunc():

    window_title = Strings.yordam_title
    
    uyariVarMi = pyautogui.locateCenterOnScreen(Strings.uyariBaslikImage, confidence=0.9)

    if uyariVarMi is not None:

        Speak(Speechs.uyariVerdi)
        im = pyautogui.screenshot(region=(500,320,345,175))
        im.save(Strings.uyariSaveFilePath)
        
        time.sleep(0.5)

        text = toText(Strings.uyariSaveFilePath)

        time.sleep(0.5)

        Speak(text)

        print(text)

        time.sleep(3)

        Speak(Speechs.uyari_islemden_cikis)

        time.sleep(0.5)

        pyautogui.press('enter')

        time.sleep(0.5)

        minimize_window(window_title)

        remove(Strings.uyariSaveFilePath)

        exit()
    else:
        Speak(Speechs.tc_demirbas_gecerli)