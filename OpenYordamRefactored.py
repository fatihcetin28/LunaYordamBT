import time
import CollectedMethodsByProcess.OpeningModules as OM
import Helpers.JAWSFSAPI as JF
import Helpers.handleScreenshot as SS


JF.StopSpeech()
time.sleep(3)

if OM.CheckIfYordamOpen():
    JF.Speak(
        "Yordam BT Zaten Açık. Lütfen Ödünç ver veya İade Al işlemlerinden birini yapınız"
    )
    time.sleep(1)
    JF.StartSpeech()
    time.sleep(1)
    exit()

JF.Speak("Yordam BT Açılıyor")

time.sleep(0.5)

OM.StartFileMaker()


time.sleep(2)
SS.takeSS()

OM.ClickYordamBTAfterFileMakerStarted()

time.sleep(1)
SS.takeSS()
JF.Speak("Yordam BT kullanıcı girişi yapılıyor.")

OM.LoginYordamBT()

SS.takeSS()
time.sleep(5)
SS.takeSS()
# OM.YordamIslemPencereAc()

OM.ClickUyeOduncIslemleriImage()
time.sleep(3)
SS.takeSS()
OM.ClickOduncIslemleriImage()
SS.takeSS()

time.sleep(1)

OM.MaxMinActiveWindow()
SS.takeSS()
time.sleep(0.5)

JF.Speak("Yordam BT Açıldı.")
SS.takeSS()
JF.StartSpeech()
