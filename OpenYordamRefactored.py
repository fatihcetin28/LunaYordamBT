import time
import CollectedMethodsByProcess.OpeningModules as OM
import Helpers.JAWSFSAPI as JF
import Helpers.handleScreenshot as SS
from Helpers.loggers import openYordamLogger

logger = openYordamLogger()

logger.debug("Yordam Açma Denemesi")

JF.StopSpeech()
time.sleep(3)

if OM.CheckIfYordamOpen():
    JF.Speak(
        "Yordam BT Zaten Açık. Lütfen Ödünç ver veya İade Al işlemlerinden birini yapınız"
    )
    time.sleep(1)
    JF.StartSpeech()
    time.sleep(1)
    logger.debug("Yordam zaten acikmis.")
    exit()

JF.Speak("Yordam BT Açılıyor")

time.sleep(0.5)

OM.StartFileMaker()
logger.debug("File Maker açılıyor")

time.sleep(2)
SS.takeSS()

OM.ClickYordamBTAfterFileMakerStarted()
logger.debug("YordamBT tıklanıyor")

time.sleep(1)
SS.takeSS()
JF.Speak("Yordam BT kullanıcı girişi yapılıyor.")

OM.LoginYordamBT()
logger.debug("Kullanıcı girişi yapılıyor")


SS.takeSS()
time.sleep(5)
SS.takeSS()
# OM.YordamIslemPencereAc()

OM.ClickUyeOduncIslemleriImage()
logger.debug("Üye ödünç işlemleri düğmesi tıklanıyor")
time.sleep(3)
SS.takeSS()
OM.ClickOduncIslemleriImage()
logger.debug("Ödünc islemler dugmesi tiklandı")
SS.takeSS()

time.sleep(1)

OM.MaxMinActiveWindow()
logger.debug("Yordam penceresi büyüt küçült")
SS.takeSS()
time.sleep(0.5)

JF.Speak("Yordam BT Açıldı.")
logger.debug("Yordam BT açılmış olmalı")
SS.takeSS()
JF.StartSpeech()
