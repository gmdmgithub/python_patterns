import speech_recognition as sr
import os
from datetime import datetime
import time

from playsound import playsound

from gtts import gTTS

lang = 'en'

def get_from_micro():

    recognition = sr.Recognizer()
    val = ""
    with sr.Microphone() as sr_mic:
        print('Say something')
        audio = recognition.listen(sr_mic)
        print('Transforming ...')
        try:
            val = recognition.recognize_google(audio, language=lang)
            print(f"Google Speech Recognition thinks you said: {val}")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
    
        greetings = ["what is your name","what's your name","tell me your name"]
        old = ["how old are you","what's your age","what is your age"]
        tel_something = ["tell something","tell me something about yourself","what do you like", "tell something about yourself", "say something about yourself"]
        exits = ['exit','bye', 'goodby', 'see you', 'quit']
        
        if val.lower() in greetings:
            speak_with_google('My name is Alex')
            return False

        if val.lower() in old:
            speak_with_google("I'm 31 years old")
            return False
        
        if val.lower() in tel_something:
            speak_with_google("I like swiming and gymnastics, I like dogs. I love my parents")
            return False

        if val.lower() in exits:
            speak_with_google('See you soon ...')
            exit()

        if val.lower().startswith('co to jest'):
            pass

    return val

def speak_with_google(string_to_speak="Nothing"):
    
    if string_to_speak and len(string_to_speak) > 0:
        tts = gTTS(text=string_to_speak, lang=lang) 
        f_name = f"audio_{datetime.now().strftime('%Y-%m-%d_%H%M%S.%f')}.mp3"
        tts.save(f_name) 
        playsound(f_name) 
        print(f"kiri: {string_to_speak}") 
        os.remove(f_name) 


l = input('Chose language (1) englis (2) polish: ')

if l == '2':
    lang = 'pl'


while True:
    
    text = get_from_micro()
    if text:
        speak_with_google(text)
    time.sleep(0.5)
