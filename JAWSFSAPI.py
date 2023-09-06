import win32com.client


# Create the COM object
# Call the SayString method
# o.SayString("Merhabalar")
# Call the RunFunction method
# o.StopSpeech()

def StopSpeech():
    o = win32com.client.Dispatch("freedomsci.jawsapi")
    o.Disable()
    # pythoncom.CoUninitialize()

def StartSpeech():
    o = win32com.client.Dispatch("freedomsci.jawsapi")
    o.Enable(True)
    # o.RunFunction("stopspeech")

def Speak(text):
    o = win32com.client.Dispatch("freedomsci.jawsapi")
    o.SayString(text)

# StartSpeech()
# a=StopSpeech()
# print(a)

# o = win32com.client.Dispatch("freedomsci.jawsapi")
# methods_and_attributes = dir(o)
# for item in methods_and_attributes:
#     print(item)
# o.Disable()
# o.Enable(True)

