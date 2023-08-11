import tkinter as tk
from tkinter import simpledialog

def userInput(title,message):

    ROOT = tk.Tk()

    ROOT.withdraw()
    # the input dialog
    USER_INP = simpledialog.askstring(title=title,
                                    prompt=message)
    return USER_INP
    # check it out
    # print("Hello", USER_INP)