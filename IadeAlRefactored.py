import Helpers.JAWSFSAPI as JF
from time import sleep
import CollectedMethodsByProcess.IadeAlModules as IM
import Helpers.YordamWindowHelper as YWM
import Helpers.handleScreenshot as SS
from Helpers.handleOduncUyari import handleUyariOdunc as handleUyari
from datetime import datetime
import Helpers.toExcel as EX
from Helpers.loggers import IadeAlLogger

logger = IadeAlLogger()

JF.StopSpeech()

sleep(3)

if not YWM.IsYordamWindowOpen():
    JF.Speak(
        "Yordam Açık Değil, lütfen önce yordamı aç modülünü kullanarak Yordamı açınız"
    )
    logger.debug("Yordam açık değilken iade denemesi")
    sleep(2)
    JF.StartSpeech()
    sleep(1)
    exit()

demirbasNo = IM.DemirbasNoAl()

sleep(1)
logger(f"{demirbasNo} iade denemesi")

data = {
    "Demirbas No": [demirbasNo],
    "Tarih": [datetime.now().date().strftime("%d-%m-%Y")],
    "Saat": [datetime.now().time().strftime("%H:%M:%S")],
}

EX.toIadeXls(data=data)

sleep(1)

SS.takeSS()
sleep(1)
YWM.MaximizeYordamWindow()
logger("Yordam penceresi büyütülüyor")

sleep(1)
SS.takeSS()
sleep(1)
IM.ClickIadeAlButton()
handleUyari()
logger("Iade al dugmesi tiklandi")
SS.takeSS()
sleep(1)

IM.DemirbasNoYaz(demirbasNo)
logger("demirbas no yazildi")
handleUyari()
SS.takeSS()
sleep(1)
SS.takeSS()
IM.IadeSuccess()
logger("iade basarili olmus olmali")

sleep(1)
SS.takeSS()
IM.ClickVazgecButton()
logger("vzgec dugmesi tiklama denemesi")
SS.takeSS()
sleep(1)
SS.takeSS()
YWM.MinimizeYordamWindow()
logger("yordam minimize edildi")
SS.takeSS()
sleep(1)
SS.takeSS()
JF.StartSpeech()
