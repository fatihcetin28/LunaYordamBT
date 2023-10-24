from Helpers.window_max_min import maximize_window
from Helpers.window_max_min import minimize_window
import Managers.WindowManager as WM


window_title = 'YordamBT s.19.2 - Sakarya Uygulamalı Bilimler Üniversitesi - KTP338'

w = WM.Window(window_title)

def MaximizeYordamWindow():
    maximize_window(window_title)

def MinimizeYordamWindow():
    minimize_window(window_title)

def IsYordamWindowOpen():
    return w.is_window_exist_by_title()