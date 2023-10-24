import Helpers.JAWSFSAPI as JF
from time import sleep
import CollectedMethodsByProcess.IadeAlModules as IM
import Helpers.YordamWindowHelper as YWM

JF.StopSpeech()

sleep(3)

if not YWM.IsYordamWindowOpen():
    JF.Speak("Yordam Açık Değil, lütfen önce yordamı aç modülünü kullanarak Yordamı açınız")
    sleep(2)
    JF.StartSpeech()
    sleep(1)
    exit()

demirbasNo=IM.DemirbasNoAl()

sleep(1)

YWM.MaximizeYordamWindow()

sleep(1)

IM.ClickIadeAlButton()

sleep(1)

IM.DemirbasNoYaz(demirbasNo)

sleep(1)

IM.IadeSuccess()

sleep(1)

IM.ClickVazgecButton()

sleep(1)

YWM.MinimizeYordamWindow()

sleep(1)

JF.StartSpeech()

