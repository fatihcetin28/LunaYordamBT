# import Managers.WindowManager as WM
# import Data.Strings as Strings
import Helpers.YordamWindowHelper as YWM

# w = WM.Window(Strings.yordam_title)

# a = w.is_window_exist_by_title()

# print(a)

a=YWM.IsYordamWindowOpen()

print(a)