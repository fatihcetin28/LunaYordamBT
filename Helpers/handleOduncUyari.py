from Helpers.JAWSFSAPI import speak
import pyautogui
import time
from Helpers.imageToText import toText
from Helpers.window_max_min import minimize_window
from os import remove
import Data.Strings as Strings
import Data.Speechs as Speechs


def handleUyariOdunc():

    window_title = Strings.yordam_title
    
    uyariVarMi = pyautogui.locateCenterOnScreen(Strings.uyariBaslik, confidence=0.9)

    if uyariVarMi is not None:

        speak(Speechs.uyariVerdi)
        im = pyautogui.screenshot(region=(500,320,345,175))
        im.save(Strings.uyariSaveFilePath)
        
        time.sleep(0.5)

        text = toText(Strings.uyariSaveFilePath)

        time.sleep(0.5)

        speak(text=text)

        time.sleep(0.5)

        speak(Speechs.uyari_islemden_cikis)

        time.sleep(0.5)

        pyautogui.press('enter')

        time.sleep(0.5)

        minimize_window(window_title)

        remove(Strings.uyariSaveFilePath)

        exit()
    else:
        speak(Speechs.tc_demirbas_gecerli)