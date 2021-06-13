import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import pyttsx3
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import pyttsx3.drivers
import sys
import random
import wolframalpha
import importlib
import pyaudio
import cv2
print("Initializing Jarvis...")

engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('6EVA26-EXKKQ6YUW4')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices) - 1].id)


def speak(text):
    print("Jarvis: " + text)
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning...")

    elif 12 <= hour < 18:
        speak("Good afternoon...")

    else:
        speak("Good evening...")

    speak("This is Jarvis...I am a virtual assistant...How can I help you ")
wishMe()


# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam.
cap = cv2.VideoCapture(0)
# To use a video file as input
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    #if faces is not None:
     #   speak("yeah")

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        speak("no")

    # Display
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k == 101:
        break

# Release the VideoCapture object
cap.release()
