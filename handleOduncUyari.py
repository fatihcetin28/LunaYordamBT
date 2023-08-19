from reallyspeak import speak
import pyautogui
import time
from imageToText import toText
from window_max_min import minimize_window
from os import remove


def handleUyariOdunc():

    window_title = 'YordamBT s.19.2 - Sakarya Uygulamalı Bilimler Üniversitesi - KTP338'
    
    uyariVarMi = pyautogui.locateCenterOnScreen(r'C:\Users\SUBU\Documents\Codebas\YordamYardimBT\uyariImages\uyariBaslik.png', confidence=0.9)
    uyariLocation = pyautogui.locateOnScreen(r'C:\Users\SUBU\Documents\Codebas\YordamYardimBT\uyariImages\uyariBaslik.png', confidence=0.9)

    print(uyariLocation)

    if uyariVarMi is not None:
        print('Hata-Uyari')
        speak("Program uyarı verdi")
        im = pyautogui.screenshot(region=(500,320,345,175))
        im.save(r"C:\Users\SUBU\Documents\Codebas\YordamYardimBT\uyari.png")
        
        time.sleep(0.5)

        text = toText(r'C:\Users\SUBU\Documents\Codebas\YordamYardimBT\uyari.png')

        time.sleep(0.5)

        speak(text=text)

        time.sleep(0.5)

        speak("Uyarı verildi ödünç verme işleminden çıkılıyor.")

        time.sleep(0.5)

        pyautogui.press('enter')

        time.sleep(0.5)

        minimize_window(window_title)

        remove(r'C:\Users\SUBU\Documents\Codebas\YordamYardimBT\uyari.png')

        exit()
    else:
        speak('Uyari Yok TC Numarası ve demirbaş numaralar geçerli görünüyor.')
        print('uyari yok')