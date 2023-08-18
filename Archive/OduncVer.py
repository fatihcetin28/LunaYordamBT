import pyautogui, time

time.sleep(2)

uyeoduncislembuton = pyautogui.locateCenterOnScreen('ButtonImages\uyeoduncislemleri.PNG', confidence=0.9)
if uyeoduncislembuton is not None:
    pyautogui.click(uyeoduncislembuton)
else:
    print("Button not found on the window.")

time.sleep(2)

oduncbutton = pyautogui.locateCenterOnScreen('ButtonImages\odunc.PNG', confidence=0.9)
if oduncbutton is not None:
    pyautogui.click(oduncbutton)
else:
    print("Button not found on the window.")

time.sleep(2)

# oduncverbutton = pyautogui.locateCenterOnScreen('oduncverbutton.PNG')
# if oduncbutton is not None:
#     pyautogui.click(oduncverbutton)
# else:
#     print("Button not found on the window.")



# time.sleep(2)
# pyautogui.write('19018679450')

# time.sleep(0.5)

# pyautogui.press("enter") 
# # oduncvertcnotamambutton = pyautogui.locateCenterOnScreen('oduncvertcnotamambutton.PNG')
# # if oduncbutton is not None:
# #     pyautogui.click(oduncvertcnotamambutton)
# # else:
# #     print("Button not found on the window.")