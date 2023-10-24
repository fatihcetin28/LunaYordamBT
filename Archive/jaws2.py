from pynput.keyboard import Controller, Key

f10 = Key.f10

k = Controller()

k.press(f10)
k.release(f10)
# keyboard = Controller()
# keyboard.press('F10')
# keyboard.release('F10')
# f10 = 