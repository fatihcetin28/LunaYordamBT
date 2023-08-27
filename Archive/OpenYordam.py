from pywinauto.application import Application
import time
import pygetwindow
from Archive.uyeoduncislemacma import uyeoduncpencereac
from Archive.reallyspeak import speak


def StartYordam():
    speak("Yordam BT Açılıyor.")
    time.sleep(1)

    app = Application(backend="uia").start(
        r"C:\Program Files\FileMaker\FileMaker Pro 19\FileMaker Pro.exe"
    )

    app = Application(backend="uia").connect(title="FileMaker Pro", timeout=100)
    # app.FileMakerPro.print_control_identifiers()

    yordamBT = app.FileMakerPro.child_window(
        title="YordamBT", control_type="ListItem"
    ).wrapper_object()
    yordamBT.double_click_input()
    # app.FileMakerPro.print_control_identifiers()

    time.sleep(2)
    passInput = app.FileMakerPro.child_window(
        auto_id="passwordBox", control_type="Edit"
    ).wrapper_object()
    passInput.type_keys("akyazimyo")
    time.sleep(0.5)
    signInButton = app.FileMakerPro.child_window(
        title="Sign in", auto_id="IDSIGNIN", control_type="Button"
    ).wrapper_object()
    signInButton.click()
    time.sleep(0.5)

    uyeoduncpencereac()

    aW = pygetwindow.getActiveWindow()
    time.sleep(0.5)
    aW.maximize()
    time.sleep(0.5)
    aW.minimize()
    time.sleep(0.5)
    # ctypes.windll.user32.MessageBoxW(0, "Yordam BT Açıldı", "Yordam BT Açıldı", 1)
    speak("Yordam BT Kütüphane Otomasyon Uygulaması Açıldı.")
