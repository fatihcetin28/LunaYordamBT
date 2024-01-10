import CollectedMethodsByProcess.OduncModules as OM
import Helpers.JAWSFSAPI as JF
import Helpers.handleOduncUyari as handle
from time import sleep
import Helpers.YordamWindowHelper as YWM
import Helpers.handleScreenshot as SS
from datetime import datetime
import Helpers.toExcel as EX
from Helpers.loggers import OduncVerLogger

logger = OduncVerLogger()

JF.StopSpeech()

sleep(3)

if not YWM.IsYordamWindowOpen():
    JF.Speak(
        "Yordam Açık Değil, lütfen önce yordamı aç modülünü kullanarak Yordamı açınız"
    )
    logger.debug("Yordam açık değilken ödünç denemesi")
    sleep(2)
    JF.StartSpeech()
    sleep(1)
    exit()

tcNo = OM.TCNoAl()

sleep(1)

demirbasNo = OM.DemirbasNoAl()

sleep(1)
logger.debug(f"tc:{tcNo}-demirbas:{demirbasNo} odunc denemesi")

data = {
    "TCNo": [tcNo],
    "Demirbas No": [demirbasNo],
    "Tarih": [datetime.now().date().strftime("%d-%m-%Y")],
    "Saat": [datetime.now().time().strftime("%H:%M:%S")],
}

EX.toOduncXls(data=data)

sleep(1)

YWM.MaximizeYordamWindow()
logger.debug("Yordam maximize edildi")

SS.takeSS()


sleep(1)

OM.OduncVerImageClick()
logger.debug("Odunc Ver dugmesi tıklandı")
SS.takeSS()

sleep(1)

handle.handleUyariOdunc()

logger.debug("Uyarı olmaması gerekir")

sleep(4)

OM.TcNoYaz(tcNo)
SS.takeSS()
logger.debug("tc no yazildi")

sleep(1)
SS.takeSS()
OM.DemirbasNoYaz(demirbasNo)
logger.debug("demirbas no yazildi")


sleep(1)

SS.takeSS()
OM.ClickVazgecButton()
logger.debug("vazgec dugmesi tiklandi")
SS.takeSS()
OM.OduncSucces()
logger.debug("odunc basarili")
SS.takeSS()
YWM.MinimizeYordamWindow()
SS.takeSS()
JF.StartSpeech()
