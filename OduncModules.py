import JAWSFSAPI as JF
from time import sleep
from inputbox import userInput
import YordamWindowModules as YWM
from ImageClickModules import ClickImage
import pyautogui
from time import sleep
from handleOduncUyari import handleUyariOdunc

JF.StopSpeech()

sleep(3)


def TCNoAl():
    JF.Speak("Lütfen TC Kimlik No Girdikten sonra devam etmek için entera basınız.")
    tcNo = userInput("Lütfen TC Kimlik No Girdikten sonra devam etmek için entera, çıkış için ESC'ye basınız.","Lütfen TC Kimlik No Giriniz." ) 
    return tcNo

def DemirbasNoAl():
    JF.Speak("Lütfen Demirbaş Seri No Girdikten sonra ödünç işlemi için entera, çıkış için ESC'ye basınız.")
    demirbasNo = userInput("Lütfen Demirbaş Seri No Girdikten sonra ödünç işlemi için entera, , çıkış için ESC'ye basınız.","Lütfen Demirbaş Seri No Giriniz." )
    return demirbasNo

def OduncVerImageClick():
    img_filepath = r'C:\Users\SUBU\Documents\Codebas\YordamYardimBT\ButtonImages\oduncverbutton.png'
    ClickImage(img_filepath, "Ödünç Ver")

def TcNoYaz(tcNo):
    pyautogui.typewrite(str(tcNo)) #tc no giriyoruz
    pyautogui.press('enter')
    sleep(0.5)
    handleUyariOdunc()

def DemirbasNoYaz(demirbasNo):
    pyautogui.typewrite(str(demirbasNo)) #demirbaş no
    pyautogui.press('enter')
    sleep(0.5)
    handleUyariOdunc()