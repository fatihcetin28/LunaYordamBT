import pyautogui
import JAWSFSAPI as JF

def ClickImage(img_filepath, img_description):
    imgLocation = pyautogui.locateCenterOnScreen(img_filepath, confidence=0.9)
    if imgLocation is not None:
        pyautogui.click(imgLocation)
        JF.Speak(f"{img_description} düğmesi tıklandı.")
        return True
    else:
        print("Button not found on the window.")
        JF.Speak(f"{img_description} düğmesi ekranda bulunamadı. Çıkış yapılıyor. Lütfen Tekrar deneyiniz.")
        return False