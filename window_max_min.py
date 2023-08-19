import pygetwindow as gw

def maximize_window(window_title):
    window = gw.getWindowsWithTitle(window_title)
    if window:
        window[0].maximize()

def minimize_window(window_title):
    window = gw.getWindowsWithTitle(window_title)
    if window:
        window[0].minimize()
# # Provide the title of the window you want to maximize
# window_title = 'YordamBT s.19.2 - Sakarya Uygulamalı Bilimler Üniversitesi - KTP338'

# # Call the function to maximize the window
# maximize_window(window_title)