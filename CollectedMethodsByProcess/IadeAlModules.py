from Helpers.inputbox import userInput
import Helpers.JAWSFSAPI as JF
import pyautogui
from time import sleep
from Helpers.handleOduncUyari import handleUyariOdunc
import Data.Speechs as speechs
import Data.Strings as strings
import Data.ImageFilaPaths as images
from Managers.ImageManager import ImageManager



def DemirbasNoAl():
    JF.Speak(speechs.iade_demirbasNoGiriniz)
    demirbasNo = userInput(strings.iadeAL_demirbasNoGiriniz, strings.iadeAl_demirbasNoGir2)
    return demirbasNo

def ClickIadeAlButton():
    imgMan = ImageManager(file_path=images.iade_al_button,description="İade Al")
    return imgMan.click()

def DemirbasNoYaz(demirbasNo):
    JF.Speak("Demirbaş no yazılıyor.")
    pyautogui.typewrite(str(demirbasNo)) #demirbaş no
    pyautogui.press('enter')
    sleep(1)
    handleUyariOdunc()

def ClickVazgecButton():
    imgMan = ImageManager(images.vazgec_button,"Vazgec")
    return imgMan.click()

def IadeSuccess():
    JF.Speak(speechs.iade_success)