import time
import CollectedMethodsByProcess.OpeningModules as OM
import Helpers.JAWSFSAPI as JF


JF.StopSpeech()
time.sleep(3)

if OM.CheckIfYordamOpen():
    JF.Speak("Yordam BT Zaten Açık. Lütfen Ödünç ver veya İade Al işlemlerinden birini yapınız")
    time.sleep(1)
    JF.StartSpeech()
    time.sleep(1)
    exit()

JF.Speak("Yordam BT Açılıyor")

time.sleep(0.5)

OM.StartFileMaker()

time.sleep(2) 

OM.ClickYordamBTAfterFileMakerStarted()

time.sleep(1)

JF.Speak("Yordam BT kullanıcı girişi yapılıyor.")

OM.LoginYordamBT()

time.sleep(5)

# OM.YordamIslemPencereAc()

OM.ClickUyeOduncIslemleriImage()
time.sleep(3)
OM.ClickOduncIslemleriImage()

time.sleep(1)

OM.MaxMinActiveWindow()

time.sleep(0.5)

JF.Speak("Yordam BT Açıldı.")

JF.StartSpeech()
