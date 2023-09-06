import JAWSFSAPI as JF
from time import sleep
import IadeAlModules as IM
import YordamWindowModules as YWM

JF.StopSpeech()

sleep(3)

demirbasNo=IM.DemirbasNoAl()

sleep(1)

YWM.MaximizeYordamWindow()

sleep(1)

IM.ClickIadeAlButton()

sleep(1)

IM.DemirbasNoYaz(demirbasNo)

sleep(1)

IM.IadeSuccess()

IM.ClickVazgecButton()

sleep(1)

YWM.minimize_window()

sleep(1)

JF.StartSpeech()

