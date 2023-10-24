from Helpers.window_max_min import maximize_window
from Helpers.window_max_min import minimize_window
import pyautogui, time
from Archive.reallyspeak import speak
from Helpers.inputbox import userInput
from Helpers.handleOduncUyari import handleUyariOdunc

# speak("Lütfen TC Kimlik No Girdikten sonra devam etmek için entera basınız.")
# time.sleep(1)
tcNo = userInput("Lütfen TC Kimlik No Girdikten sonra devam etmek için entera, çıkış için ESC'ye basınız.","Lütfen TC Kimlik No Giriniz." ) 

# print(tcNo)
if tcNo is None:
    speak("TC No Girmediniz. Ödünç verme işleminden çıkılıyor")

# speak("Lütfen Demirbaş Seri No Girdikten sonra ödünç işlemi için entera basınız.")
time.sleep(0.5)
demirbasNo = userInput("Lütfen Demirbaş Seri No Girdikten sonra ödünç işlemi için entera, , çıkış için ESC'ye basınız.","Lütfen Demirbaş Seri No Giriniz." )

if tcNo is None:
    speak("Demirbas No Girmediniz. Ödünç verme işleminden çıkılıyor")

time.sleep(0.5)

# Provide the title of the window you want to maximize
window_title = 'YordamBT s.19.2 - Sakarya Uygulamalı Bilimler Üniversitesi - KTP338'

# Call the function to maximize the window
maximize_window(window_title)

oduncverbutton = pyautogui.locateCenterOnScreen(r'C:\Users\SUBU\Documents\Codebas\YordamYardimBT\ButtonImages\oduncverbutton.png', confidence=0.9)
if oduncverbutton is not None:
    pyautogui.click(oduncverbutton)
else:
    print("Button not found on the window.")
    speak("Odunç ver düğmesi ekranda bulunamadı. Çıkış yapılıyor. Lütfen Tekrar deneyiniz.")
    
    

time.sleep(2)

pyautogui.typewrite(str(tcNo)) #tc no giriyoruz
pyautogui.press('enter')
time.sleep(1)

handleUyariOdunc()
   
pyautogui.typewrite(str(demirbasNo)) #demirbaş no
pyautogui.press('enter')

handleUyariOdunc()

speak("Ödünç verme işlemi başarılı.")

minimize_window(window_title)
