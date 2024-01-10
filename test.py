# import Managers.WindowManager as WM
# import Data.Strings as Strings
# import Helpers.YordamWindowHelper as YWM

# # w = WM.Window(Strings.yordam_title)

# # a = w.is_window_exist_by_title()

# # print(a)

# a=YWM.IsYordamWindowOpen()

# print(a)

# import Helpers.handleScreenshot as SS
# from time import sleep

# SS.takeSS()
# sleep(2)
# SS.takeSS()
from Helpers.loggers import openYordamLogger

l = openYordamLogger()
l.debug("deneme22")
