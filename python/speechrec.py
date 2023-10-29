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
        #Using Whisper
        text = r.recognize_whisper(audio, language="english")
        #We need to remove any punctuation and make it lowercase before we put it through wordfilter.
        text = text.lower()
        #Using regex, remove punctuation.
        text= re.sub(r'[^\w\s]', '', text)
        swore = check_speech(text)
    except sr.UnknownValueError:
        print("Whisper could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Whisper")

    if swore:
        print("Discoure paused, watch the langauge!")



print("Welcome to the Discourse Mediator app! When you are ready, start discussing, if anyone uses innapropriate language, it will be detected and the system will give a warning.")

while(True):
    runtime()