from Managers.WindowManager import Window

w = Window("Defteri")

a = w.is_window_exist_by_title()
print(a)

print(w.is_window_maximized())
print(w.is_window_minimized())