import pyautogui
import os
from datetime import datetime
from time import sleep

folder = "Screenshots"
script_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(script_path)
grandparent_directory = os.path.abspath(os.path.join(parent_directory, ".."))
SSFolder = os.path.join(grandparent_directory, folder)


print("girdi")


def takeSS():
    # Get the current time
    current_time = datetime.now().time()

    # Format and print the current time
    formatted_time = current_time.strftime("%H%M%S")

    # Get the current date
    current_date = datetime.now().date()

    # Format and print the current date
    formatted_date = current_date.strftime("%d%m%y")
    # print("Current Date (formatted):", formatted_date)

    ssName = f"{formatted_date}-{formatted_time}"

    ss = pyautogui.screenshot()
    ssPath = os.path.join(SSFolder, f"{ssName}.png")
    ss.save(ssPath)


# takeSS()
# sleep(2)
# takeSS()
