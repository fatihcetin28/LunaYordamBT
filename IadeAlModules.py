from inputbox import userInput
import JAWSFSAPI as JF
import ImageClickModules as IMGClick
import pyautogui
from time import sleep
from handleOduncUyari import handleUyariOdunc




def DemirbasNoAl():
    JF.Speak("Lütfen Demirbaş Seri No Girdikten sonra ödünç işlemi için entera, çıkış için ESC'ye basınız.")
    demirbasNo = userInput("Lütfen Demirbaş Seri No Girdikten sonra iade alma işlemi için entera, çıkış için ESC'ye basınız.","Lütfen Demirbaş Seri No Giriniz." )
    return demirbasNo

def ClickIadeAlButton():
    IMGClick.ClickImage(r'C:\Users\SUBU\Documents\Codebas\YordamYardimBT\ButtonImages\iadealbutton.png',"İade Al")

def DemirbasNoYaz(demirbasNo):
    pyautogui.typewrite(str(demirbasNo)) #demirbaş no
    pyautogui.press('enter')
    sleep(1)
    handleUyariOdunc()

def ClickVazgecButton():
    IMGClick.ClickImage(r'C:\Users\SUBU\Documents\Codebas\YordamYardimBT\ButtonImages\vazgecButton.PNG',"Vazgec")

def IadeSuccess():
    JF.Speak("İade alma işlemi başarılı.")