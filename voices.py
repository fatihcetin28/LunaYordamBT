import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print("Voice ID:", voice.id)
    print("Name:", voice.name)

engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\Vocalizer Expressive yelda premium-high 22kHz')
engine.say('Merhaba dünya')
engine.runAndWait()

print(engine.getProperty('voice'))