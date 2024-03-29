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
logger.debug(f"{demirbasNo} iade denemesi")

data = {
    "Demirbas No": [demirbasNo],
    "Tarih": [datetime.now().date().strftime("%d-%m-%Y")],
    "Saat": [datetime.now().time().strftime("%H:%M:%S")],
}

try:
    EX.toIadeXls(data=data)
except Exception as e:
    logger.debug(e)

sleep(1)

SS.takeSS()
sleep(1)
YWM.MaximizeYordamWindow()
logger.debug("Yordam penceresi büyütülüyor")

sleep(1)
SS.takeSS()
sleep(1)
IM.ClickIadeAlButton()
handleUyari()
logger.debug("Iade al dugmesi tiklandi")
SS.takeSS()
sleep(1)

logger.debug("demirbas no yazildi")
IM.DemirbasNoYaz(demirbasNo)

handleUyari()
SS.takeSS()
sleep(1)
SS.takeSS()
IM.IadeSuccess()
logger.debug("iade basarili olmus olmali")

sleep(1)
SS.takeSS()
IM.ClickVazgecButton()
logger.debug("vazgec dugmesi tiklama denemesi")
SS.takeSS()
sleep(1)
SS.takeSS()
YWM.MinimizeYordamWindow()
logger.debug("yordam minimize edildi")
SS.takeSS()
sleep(1)
SS.takeSS()
JF.StartSpeech()
