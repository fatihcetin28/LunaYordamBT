from pywinauto import keyboard


def StopSpeaking():
    keyboard.send_keys(
        "{VK_INSERT down}" "{SPACE down}" "s" "{VK_INSERT up}" "{SPACE up}"
    )


def StartSpeaking():
    keyboard.send_keys(
        "{VK_INSERT down}" "{SPACE down}" "s" "{VK_INSERT up}" "{SPACE up}"
    )

    # keyboard.send_keys("{LWIN down}""{VK_LSHIFT down}""s""{VK_LSHIFT up}""{LWIN up}")
