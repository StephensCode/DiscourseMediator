import pyaudio
import speech_recognition as sr
from wordfilter import Wordfilter
import whisper
import re



def check_speech(text):
    wordfilter = Wordfilter()
    return wordfilter.blacklisted(text)

# Obtaining audio from the microphone

def runtime():
    swore = False
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Testing now! ")
        audio = r.listen(source)
    # Using Whipser
    try:
        text = r.recognize_whisper(audio, language="english")
        print("Whisper thinks you said " + text)
        #We need to remove any punctuation before we put it through wordfilter.
        text = text.lower()
        text= re.sub(r'[^\w\s]', '', text)
        print(text)
        swore = check_speech(text)
    except sr.UnknownValueError:
        print("Whisper could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Whisper")

    if swore:
        print("Discoure paused, watch the langauge!")

while(True):
    runtime()