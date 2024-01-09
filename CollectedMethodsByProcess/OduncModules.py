import Helpers.JAWSFSAPI as JF
from time import sleep
from Helpers.inputbox import userInput
import pyautogui
from time import sleep
from Helpers.handleOduncUyari import handleUyariOdunc
import Data.Speechs as speechs
import Data.ImageFilaPaths as images
from Managers.ImageManager import ImageManager


def TCNoAl():
    JF.Speak(speechs.odunc_tc_no_giriniz)
    tcNo = userInput(speechs.odunc_tc_no_giriniz, speechs.odunc_tc_no_giriniz2)
    return tcNo


def DemirbasNoAl():
    JF.Speak(speechs.odunc_demirbasNoGiriniz)
    demirbasNo = userInput(
        speechs.odunc_demirbasNoGiriniz, speechs.odunc_demirbasNoGiriniz2
    )
    return demirbasNo


def OduncVerImageClick():
    img_filepath = images.odunc_ver_button
    imgMan = ImageManager(img_filepath, "Ödünç Ver")
    return imgMan.click()


def TcNoYaz(tcNo):
    JF.Speak("TC No yazılıyor.")
    pyautogui.typewrite(str(tcNo))  # tc no giriyoruz
    pyautogui.press("enter")
    sleep(1)
    handleUyariOdunc()


def DemirbasNoYaz(demirbasNo):
    JF.Speak("Demirbaş No Yazılıyor.")
    pyautogui.typewrite(str(demirbasNo))  # demirbaş no
    pyautogui.press("enter")
    sleep(1)
    handleUyariOdunc()


def OduncSucces():
    JF.Speak(speechs.odunc_success)


def ClickVazgecButton():
    imgMan = ImageManager(images.vazgec_button, "Vazgec")
    return imgMan.click()
