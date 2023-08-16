import time
from reallyspeak import speak
import OpeningModules as OM
import Jaws

Jaws.StopSpeaking()

speak("Yordam BT Açılıyor.")

time.sleep(0.5)

OM.StartFileMaker()

time.sleep(1.5)

OM.ClickYordamBTAfterFileMakerStarted()

time.sleep(1.5)

OM.LoginYordamBT()

time.sleep(0.5)

OM.YordamIslemPencereAc()

time.sleep(0.5)

OM.MaxMinActiveWindow()

time.sleep(0.5)

speak("Yordam BT Açıldı.")

Jaws.StartSpeaking()
