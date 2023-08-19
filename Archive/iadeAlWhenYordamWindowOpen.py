from window_max_min import maximize_window
from window_max_min import minimize_window
import pyautogui, time
from reallyspeak import speak
from inputbox import userInput
from handleOduncUyari import handleUyariOdunc

demirbasNo = userInput("Lütfen Demirbaş Seri No Girdikten sonra ödünç işlemi için entera, çıkış için ESC'ye basınız.","Lütfen Demirbaş Seri No Giriniz." )

time.sleep(0.5)

# Provide the title of the window you want to maximize
window_title = 'YordamBT s.19.2 - Sakarya Uygulamalı Bilimler Üniversitesi - KTP338'

# Call the function to maximize the window
maximize_window(window_title)

time.sleep(0.5)

iadealbutton = pyautogui.locateCenterOnScreen(r'C:\Users\SUBU\Documents\Codebas\YordamYardimBT\ButtonImages\iadealbutton.png', confidence=0.9)
if iadealbutton is not None:
    pyautogui.click(iadealbutton)
else:
    print("Button not found on the window.")
    speak("İade düğmesi ekranda bulunamadı.")
    

time.sleep(1)

pyautogui.typewrite(str(demirbasNo)) #demirbas no giriyoruz
pyautogui.press('enter')
time.sleep(0.5)

handleUyariOdunc()

speak("İade verme işlemi başarılı.")

minimize_window(window_title)