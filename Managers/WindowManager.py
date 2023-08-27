import pygetwindow as gw
from time import sleep
class Window:
    
    def __init__(self, window_title="") -> None:
        self.window_title=window_title

    def window_object(self):
        window = gw.getWindowsWithTitle(self.window_title)
        if window:
            return window[0]

    def maximize(self):
        self.window_object().maximize()

    def minimize(self):
        self.window_object().minimize()

    def maximize_active_window(self):
        aW = gw.getActiveWindow()
        sleep(0.5)
        aW.maximize()

    def minimize_active_window(self):
        aW = gw.getActiveWindow()
        sleep(0.5)
        aW.minimize()

    def max_min_active_window(self):
        self.maximize_active_window()
        sleep(0.5)
        self.minimize_active_window()

    def activate(self):
        # only activates does not bring foreground
        self.window_object().activate()

    def is_window_exist_by_title(self) -> bool:
        return self.window_object() is not None

    def is_window_active(self) -> bool:
        return self.window_object().isActive

    def is_window_maximized(self) -> bool:
        return self.window_object().isMaximized

    def is_window_minimized(self) -> bool:
        return self.window_object().isMinimized
    
    def get_active_window(self):
        return gw.getActiveWindow()

    def hide(self):
        self.window_object().hide()

    def show(self):
        self.window_object().show()

