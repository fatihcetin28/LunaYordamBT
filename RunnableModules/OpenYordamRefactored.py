import time
# from reallyspeak import speak
import CollectedMethodsByProcess.OpeningModules as OM
import Helpers.JAWSFSAPI as JF

JF.StopSpeech()
time.sleep(3)

JF.Speak("Yordam BT Açılıyor")

time.sleep(0.5)

OM.StartFileMaker()

time.sleep(2) 

OM.ClickYordamBTAfterFileMakerStarted()

time.sleep(1)

OM.LoginYordamBT()

time.sleep(3)

OM.YordamIslemPencereAc()

time.sleep(0.5)

OM.MaxMinActiveWindow()

time.sleep(0.5)

JF.Speak("Yordam BT Açıldı.")

JF.StartSpeech()
