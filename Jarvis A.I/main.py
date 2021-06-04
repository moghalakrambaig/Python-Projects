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
import smtplib
import pywhatkit

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


print("akram")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except sr.UnknownValueError:
        speak("sorry...please make sure your voice is clear")
        query = takeCommand()
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mabpc007@gmail.com', 'thetoppertenmab')
    server.sendmail('mabpc007@gmail.com', 'moghalakrambaig8@gmail.com', 'hiii')
    server.close()

print("akram")
wishMe()
while True:
    query = takeCommand()

    if 'wikipedia' in query.lower():
        speak("Searching wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak(results)

    elif 'assalamu alaikum' in query.lower():
        speak("waalaikum assalam... mai aapki kyaa madath karr sakti hoon")

    elif 'khairiyat' in query.lower():
        speak("alhamdulillah...aap khairiyath")

    elif 'email to harry' in query.lower():
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "moghalakrambaig8@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email") 

    elif 'no you are wrong' in query.lower():
        speak("how dare you to tell me that")

    elif 'what is your date of birth' in query.lower():
        speak("I was Born on 25 may 2020 at 1:10AM IST")

    elif 'close this program' in query.lower():
        codeExe = "Code.exe"
        os.system("taskkill /f /im " + codeExe)

    elif 'snake game' in query.lower():
        snake_path = 'C:/Users/AMEER/Desktop/Snake/Game/snake.py'
        os.startfile(snake_path)
        speak("opening snake game")



    #elif 'what is my phone number' in query.lower():
      #  number()


    elif 'open youtube' in query.lower():

        url = "www.youtube.com"
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        speak("opening youtube")


    elif 'close youtube' in query.lower():
        browserExe = "chrome.exe"
        os.system("taskkill /f /im " + browserExe)


    elif 'open editor' in query.lower():
        filmora_path = 'C:/Program Files (x86)/Wondershare/Wondershare Filmora (CPC)/Wondershare Filmora9'
        os.startfile(filmora_path)
        speak("opening filmora")

    elif 'close editor' in query.lower():
        editorExe = "CamtasiaStudio.exe"
        os.system("taskkill /f /im " + editorExe)

    elif 'play music' in query.lower():
        songsdir = "C:\\Users\\AMEER\\Music\\music"
        songs = os.listdir(songsdir)
        os.startfile(os.path.join(songsdir, songs[0]))
        speak("playing music")



    elif 'time now' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"time is {strTime}")


    elif 'open google' in query.lower():
        speak("opening google")
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
        os.startfile(chrome_path)



    elif 'close google' in query.lower():
        browserExe = "chrome.exe"
        os.system("taskkill /f /im " + browserExe)




    elif 'gaana' in query.lower():
        command = query
        query = query.replace("play", "")
        webbrowser.open('https://gaana.com/search/' + command)
        speak("opening gaana")


    elif 'play' in query.lower() or 'youtube' in query.lower() or 'from youtube' in query.lower() or 'videos' in query.lower():
        command1 = query.replace('play','')
        #webbrowser.open('https://www.youtube.com/results?search_query=' + command1)
        speak("Playing"+ command1)
        pywhatkit.playonyt(command1)
        

    elif 'who are you' in query.lower() or 'who created you' in query.lower():
        speak("MY name is jarvis...Iam a virtual assistant created by mister moghal Akram baig")

    elif 'according to google' in query.lower():
        command2 = query
        url = 'https://www.google.com/search?q=' + command2
        speak('opening google')

        webbrowser.open(url)



    elif 'best college in the world' in query.lower():
        speak("siddhartha institute of technology and sciences")

    elif 'what can you do for me' in query.lower():
        speak("I can do anything for you...")


    elif 'kya hua jarvis' in query.lower():
        speak("kuch nahi marey bhoi")

    elif 'thank you' in query or 'abort' in query or 'stop' in query:
        speak("Thank you... have a nice day ")
        sys.exit()

    elif 'shutdown' in query.lower():
        os.system('shutdown -s')


    elif 'restart' in query.lower():
        os.system('shutdown -r')


    elif 'ip' in query.lower():
        os.system('ipconfig')

    elif "whats up" in query or 'how are you' in query:
        stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
        speak(random.choice(stMsgs))
    else:
        try:
            try:
                command3 = query
                speak('searching...')
                res = client.query(query)
                results = next(res.results).text
                speak(results)
            except:
                command4 = query
                results = wikipedia.summary(query, sentences=2)
                speak(results)

        except:
            command5 = query
            speak("opening google...")
            url = 'https://www.google.com/search?q=' + command5
            webbrowser.open(url)
