from gtts import gTTS
import os
from playsound import playsound

def speak(text):
    # Create a gTTS object with Turkish as the language
    tts = gTTS(text=text, lang='tr')
    # Save the speech as an audio file
    tts.save('output.mp3')

    playsound('output.mp3')
    os.remove('output.mp3')





