from pywinauto.application import Application
import pyautogui
import time
import pygetwindow


def StartFileMaker():
    app = Application(backend="uia").start(
        r"C:\Program Files\FileMaker\FileMaker Pro 19\FileMaker Pro.exe"
    )


def ConnectFileMakerAndReturnApp():
    app = Application(backend="uia").connect(title="FileMaker Pro", timeout=100)
    return app


def ClickYordamBTAfterFileMakerStarted():
    app = ConnectFileMakerAndReturnApp()
    yordamBT = app.FileMakerPro.child_window(
        title="YordamBT", control_type="ListItem"
    ).wrapper_object()
    yordamBT.double_click_input()

def LoginYordamBT():
    app = ConnectFileMakerAndReturnApp()
    passInput = app.FileMakerPro.child_window(
        auto_id="passwordBox", control_type="Edit"
    ).wrapper_object()
    passInput.type_keys("akyazimyo")
    time.sleep(0.5)
    signInButton = app.FileMakerPro.child_window(
        title="Sign in", auto_id="IDSIGNIN", control_type="Button"
    ).wrapper_object()
    signInButton.click()


def ClickUyeOduncIslemleriImage():
    uyeoduncislembuton = pyautogui.locateCenterOnScreen(
        r"C:\Users\SUBU\Documents\Codebas\YordamYardimBT\ButtonImages\uyeoduncislemleri.png",
        confidence=0.9,
    )
    if uyeoduncislembuton is not None:
        pyautogui.click(uyeoduncislembuton)
    else:
        print("Button not found on the window.")


def ClickOduncIslemleriImage():
    oduncbutton = pyautogui.locateCenterOnScreen(
        r"C:\Users\SUBU\Documents\Codebas\YordamYardimBT\ButtonImages\odunc.png",
        confidence=0.9,
    )
    if oduncbutton is not None:
        pyautogui.click(oduncbutton)
    else:
        print("Button not found on the window.")


def YordamIslemPencereAc():
    ClickUyeOduncIslemleriImage()
    time.sleep(2)
    ClickOduncIslemleriImage()


def MaximizeActiveWindow():
    aW = pygetwindow.getActiveWindow()
    time.sleep(0.5)
    aW.maximize()


def MinimizeActiveWindow():
    aW = pygetwindow.getActiveWindow()
    time.sleep(0.5)
    aW.minimize()


def MaxMinActiveWindow():
    MaximizeActiveWindow()
    MinimizeActiveWindow()
