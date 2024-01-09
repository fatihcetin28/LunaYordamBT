from pywinauto.application import Application
import time
import pygetwindow
import pythoncom
import Data.Strings as strings
import Data.ImageFilaPaths as images
from Managers.ImageManager import ImageManager
from Managers.YordamManager import CheckIfYordamOpen


def __init__(self):
    pythoncom.CoInitializeEx(pythoncom.COINIT_APARTMENTTHREADED)


def StartFileMaker():
    app = Application(backend="uia").start(strings.file_maker_exe_path)


def ConnectFileMakerAndReturnApp():
    app = Application(backend="uia").connect(
        title=strings.file_maker_title, timeout=100
    )
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
    passInput.type_keys(strings.yordam_sifre)
    time.sleep(0.5)
    signInButton = app.FileMakerPro.child_window(
        title="Sign in", auto_id="IDSIGNIN", control_type="Button"
    ).wrapper_object()
    signInButton.click()


def ClickUyeOduncIslemleriImage():
    imgMan = ImageManager(images.uye_odunc_islemleri_button, "Üye Ödunc İşlemleri")
    imgMan.click()


def ClickOduncIslemleriImage():
    imgMan2 = ImageManager(images.odunc_islemleri, "Odünç İşlemleri")
    print(images.odunc_islemleri)
    print(f"{imgMan2.file_path} : imgMan2 file path")
    imgMan2.click()


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


def CheckIFYordamOpenAtOpening():
    return CheckIfYordamOpen()
