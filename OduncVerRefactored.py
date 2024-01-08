import CollectedMethodsByProcess.OduncModules as OM
import Helpers.JAWSFSAPI as JF
from time import sleep
import Helpers.YordamWindowHelper as YWM
import Helpers.handleScreenshot as SS

JF.StopSpeech()

sleep(3)

if not YWM.IsYordamWindowOpen():
    JF.Speak(
        "Yordam Açık Değil, lütfen önce yordamı aç modülünü kullanarak Yordamı açınız"
    )
    sleep(2)
    JF.StartSpeech()
    sleep(1)
    exit()

tcNo = OM.TCNoAl()

sleep(1)

demirbasNo = OM.DemirbasNoAl()

sleep(1)

YWM.MaximizeYordamWindow()

SS.takeSS()


sleep(1)

OM.OduncVerImageClick()
SS.takeSS()

sleep(1)

OM.TcNoYaz(tcNo)
SS.takeSS()

sleep(1)
SS.takeSS()
OM.DemirbasNoYaz(demirbasNo)


sleep(1)

SS.takeSS()
OM.ClickVazgecButton()
SS.takeSS()
OM.OduncSucces()
SS.takeSS()
YWM.MinimizeYordamWindow()
SS.takeSS()
JF.StartSpeech()
