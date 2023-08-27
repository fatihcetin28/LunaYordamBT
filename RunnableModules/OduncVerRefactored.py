import CollectedMethodsByProcess.OduncModules as OM
import Helpers.JAWSFSAPI as JF
from time import sleep
import Helpers.YordamWindowHelper as YWM

JF.StopSpeech()

sleep(3)

tcNo= OM.TCNoAl()

sleep(1)

demirbasNo = OM.DemirbasNoAl()

sleep(1)

YWM.MaximizeYordamWindow()

sleep(1)

OM.OduncVerImageClick()

sleep(1)

OM.TcNoYaz(tcNo)

sleep(1)

OM.DemirbasNoYaz(demirbasNo)

sleep(1)

OM.ClickVazgecButton()

OM.OduncSucces()

YWM.MinimizeYordamWindow()

JF.StartSpeech()


