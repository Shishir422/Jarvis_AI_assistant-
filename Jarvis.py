import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys
import smtplib


print("Initializing Jarvis...")


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak("Good Morning")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Jarvis. How may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5,phrase_time_limit=8)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")


    except Exception as e:
	# print(e)
        print("Repeat")        
        return  "none"
    query = query.lower()
    return query
    

def TaskExecution():
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
                webbrowser.open("https://www.youtube.com/") 

        elif 'open classroom' in query:
                webbrowser.open("https://classroom.google.com/h/") #link of google classroom

        elif 'open gmail' in query:
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox/")

        elif 'open monkey' in query:
                webbrowser.open("https://monkeytype.com/") #link for monkey. Monkey is a typing platform.

        elif 'open studio' in query:
                webbrowser.open("")

        elif 'sleep' in query or "sleep now" in query:
            speak("Okay sir. I am going to sleep you can call me anytime.")
            break

        elif 'open notepad' in query.lower():
                apath = "C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(apath)

        elif 'open command prompt' in query:
                os.system("start cmd")

        elif 'close notepad' in query:
                speak("okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")      

        elif 'how are you' in query:
                speak("I am fine Sir. What about you")

        elif 'i am fine' in query:
                speak("Nice to hear that sir!")

        elif 'i am not fine'in query or 'i am upset' in query:
                speak("ohh! Dont  wories sir. Just Belive in God. ")

        elif 'thanks' in query or 'thank you' in query:
                speak('You are most welcome sir!')

        elif 'who are you' in query:
            speak('I am Jarvis created by Shishir!')
        










if __name__ == "__main__":
    while True:
        permission = takeCommand()
        if "wake up" in permission:
            TaskExecution()
        elif "goodbye" in permission:
            speak("Thanks for using me sir, have a good day")
            sys.exit()