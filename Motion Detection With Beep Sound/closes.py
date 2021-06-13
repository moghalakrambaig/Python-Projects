
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyttsx3.drivers
import sys
import random



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[len(voices)-1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def tell():

    query = takeCommand()

    if 'when were you born' or 'what is your date of birth' in query.lower():
        speak("I was Born on 25 may 2020")
    
    else:
        speak("sorry")

tell()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except sr.UnknownValueError:
        speak("sorry...please make sure your voice is clear")
        query = takeCommand()
    return query        




takeCommand()


