import Helpers.JAWSFSAPI as JF
from time import sleep
import CollectedMethodsByProcess.IadeAlModules as IM
import Helpers.YordamWindowHelper as YWM
import Helpers.handleScreenshot as SS
from datetime import datetime
import Helpers.toExcel as EX


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

demirbasNo = IM.DemirbasNoAl()

sleep(1)

data = {
    "Demirbas No": [demirbasNo],
    "Tarih": [datetime.now().date().strftime("%d-%m-%Y")],
    "Saat": [datetime.now().time().strftime("%H:%M:%S")],
}

EX.toIadeXls(data=data)

sleep(1)

SS.takeSS()

YWM.MaximizeYordamWindow()

sleep(1)
SS.takeSS()
IM.ClickIadeAlButton()
SS.takeSS()
sleep(1)

IM.DemirbasNoYaz(demirbasNo)
SS.takeSS()
sleep(1)
SS.takeSS()
IM.IadeSuccess()

sleep(1)
SS.takeSS()
IM.ClickVazgecButton()
SS.takeSS()
sleep(1)
SS.takeSS()
YWM.MinimizeYordamWindow()
SS.takeSS()
sleep(1)
SS.takeSS()
JF.StartSpeech()
