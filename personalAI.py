import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyautogui
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>+12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("I am Aryan. how may I help you ?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ji")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing ")
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said : {query}\n")
    except Exception as e:
        print(e)
        print("Can you please repeat it")
        return "None"
    return query 


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'close this tab' in query:
            pyautogui.hotkey("alt", "f4")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            print(strTime)
        elif 'open visual studio' in query:
            codePath = "C:\\Users\\aryan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'shut down' in query:
            exit()
         