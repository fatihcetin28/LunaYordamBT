import pyautogui, time

def uyeoduncpencereac():
    time.sleep(2)
    uyeoduncislembuton = pyautogui.locateCenterOnScreen(r'C:\Users\SUBU\Documents\Codebas\YordamYardimBT\ButtonImages\uyeoduncislemleri.png', confidence=0.9)
    if uyeoduncislembuton is not None:
        pyautogui.click(uyeoduncislembuton)
    else:
        print("Button not found on the window.")

    time.sleep(2)

    oduncbutton = pyautogui.locateCenterOnScreen(r'C:\Users\SUBU\Documents\Codebas\YordamYardimBT\ButtonImages\odunc.png', confidence=0.9)
    if oduncbutton is not None:
        pyautogui.click(oduncbutton)
    else:
        print("Button not found on the window.")

    time.sleep(2)