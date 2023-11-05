import pyaudio
import speech_recognition as sr
from better_profanity import profanity
import whisper
import re
import sys


    
# Obtaining audio from the microphone

def runtime():
    swore = False
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Testing now! ")
        audio = r.listen(source)

    try:
        #Using Whisper
        text = r.recognize_whisper(audio, language="english")
        swore = profanity.contains_profanity(text)
        print(text)
    except sr.UnknownValueError:
        print("Whisper could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Whisper")

    if swore:
        print("explicit")


#Outside

print("explicit")
sys.stdout.flush()