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
from pygame import mixer 


engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('6EVA26-EXKKQ6YUW4')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices) - 1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

# Starting the mixer 
mixer.init() 
  
# Loading the song 
mixer.music.load("song.mp3") 
  
# Setting the volume 
mixer.music.set_volume(0.7) 
  

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

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        #speak("noo")
        # Start playing the song 
        mixer.music.play()
    # Display
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k == 101:
        break

# Release the VideoCapture object
cap.release()
