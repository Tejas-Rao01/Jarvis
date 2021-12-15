import pyttsx3
from decouple import config
from datetime import datetime
import speech_recognition as sr
from random import choice
from utils import opening_text

import os
import subprocess as sp

USERNAME  = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('sapi5')

engine.setProperty('rate', 190)

engine.setProperty('volume', 1.0)


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()



def greet_user():
    hour = datetime.now().hour
    [greeting, farewell] = wishes()
    speak(f"{greeting} {USERNAME}")
    speak(f"I am {BOTNAME}. How may I be of service?")

def wishes():
    hour = datetime.now().hour
    farewell = 'Good Day'
    if (hour >= 21) or (hour <= 2):
        farewell = 'Good Night'
    if (hour >= 6) and (hour <12):
        greeting = 'Good Morning'
        
    elif (hour <= 16) and (hour >=12):
        greeting = 'Good Afternoon'
        
    else:
        greeting = 'Good Evening'
        

    return [greeting, farewell]

def take_user_input():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... ")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print('Recognizing')
            query = r.recognize_google(audio, language='eng-in')
            if not 'exit' in query or 'stop' in query:
                speak(choice(response_txt))
            else:
                [greeting,farewell] = wishes()
                speak(f"{farewell}, see you later!")

            exit()
        except Exception:
            speak("Sorry, could you repeat that?")
            query = 'None'
    return query




paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    #'discord': "C:\\Users\\ashut\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'age of empires': "C:\\Users\\My PC\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Steam\\Age of Empires II Definitive Edition.url"
}



def camera():
    sp.run('start microsoft.windows.camera', shell = True )

def open_notepad():
    os.startfile(paths['notepad'])


