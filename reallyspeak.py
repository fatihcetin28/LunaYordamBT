import pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\Vocalizer Expressive yelda premium-high 22kHz')
def speak(text):
    engine.say(text)
    engine.runAndWait()