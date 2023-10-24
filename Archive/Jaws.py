from pywinauto import keyboard
import pyautogui, time
# import pygetwindow as gw
# # from pygetwindowMaximize import maximize_window
# # from pygetwindowMaximize import minimize_window

# # def StopSpeaking():
# #     keyboard.send_keys(
# #         "{INS down}" "{SPACE down}" "{INS up}" "{SPACE up}" "{s down}" "{s up}"
# #     )


# # def StartSpeaking():
# #     keyboard.send_keys(
# #         "{INS down}" "{SPACE down}" "{INS up}" "{SPACE up}" "{s down}" "{s up}"
# #     )



# def StopSpeaking():
#     # pyautogui.keyDown('space')
#     pyautogui.press('insert')
#     # pyautogui.keyUp('space')
#     # pyautogui.press('s')


# def StartSpeaking():
#     pyautogui.keyDown('space')
#     pyautogui.press('insert')
#     pyautogui.keyUp('space')
#     time.sleep(1)  # Add a short delay
#     pyautogui.press('s')
#     print("basıldı")

# # Specify the target window title
# target_window_title = "JAWS profesyonel"

# # Get the list of windows with the specified title
# windows = gw.getWindowsWithTitle(target_window_title)

# # Check if a window with the specified title was found
# if windows:
#     target_window = windows[0]  # Assuming there's only one window with the specified title
    
#     # Bring the window to the foreground using pyautogui
#     target_window.activate()
#     print("Aktive edildi")
    
#     # Introduce a delay to allow time for the window to activate
#     time.sleep(1)
# else:
#     print(f"No window with the title '{target_window_title}' found.")

# # StopSpeaking()
# StartSpeaking()

#     # keyboard.send_keys("{LWIN down}""{VK_LSHIFT down}""s""{VK_LSHIFT up}""{LWIN up}")

# # >>> pyautogui.keyDown('shift')  # hold down the shift key
# # >>> pyautogui.press('left')     # press the left arrow key
# # >>> pyautogui.press('left')     # press the left arrow key
# # >>> pyautogui.press('left')     # press the left arrow key
# # >>> pyautogui.keyUp('shift')    # release the shift key

# pyautogui.keyDown('ctrl')
# pyautogui.keyDown('alt')
# pyautogui.press('d')
# pyautogui.keyUp('alt')
# pyautogui.keyUp('ctrl')

# pyautogui.hotkey('ctrl', 'alt', 'd', interval=0.25)
# pyautogui.keyDown('ctrl')
# pyautogui.keyDown('alt')
# pyautogui.press('f10')
# pyautogui.keyUp('d')
# pyautogui.keyUp('alt')
# pyautogui.keyUp('ctrl')
keyboard.send_keys("{F10}")