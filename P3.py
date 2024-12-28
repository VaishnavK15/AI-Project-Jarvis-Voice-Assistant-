import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour >= 0 and hour < 12):
        speak("Good Morning")
    elif(hour >= 12 and hour < 18):
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Jarvis Here! How may i help you sir?")

def AboutJarvis():
    speak("Hello I Am Jarvis AI!")
    speak("Build Using Python Programming Language By Sir...Vaishnav....Kokate")
    speak("Speed One Terahertz")
    speak("Memory Capacity 1 Zettabyte")
    speak("You Can Use Me For Automation of your device......Thank You!!")

def search_google(query):
    search_url =  f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)

def takeCommand():#It Takes Micorphone Command Input!
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing......")
        query = r.recognize_google(audio , language='en-in')
        print(f"User Said:{query}\n")
    except Exception as e:
        print(e)
        print("Say That Again Please!")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According To Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open gpt' in query:
            webbrowser.open("chat.openai.com")
        elif 'play music for me' in query:
            music_dir = 'C:\\Users\\Vaishnav T Kokate\\OneDrive\\Desktop\\songs'
            songs = os.listdir(music_dir)
            random_song = random.choice(songs)
            print("Now Playing:",random_song)
            os.startfile(os.path.join(music_dir,random_song))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir The Time Is {strTime}")
        elif 'open vs code' in query:
            code_path = "C:\\Users\Vaishnav T Kokate\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            subprocess.Popen(code_path)
        elif 'tell me about you' in query:
            AboutJarvis()
        elif 'search on google for' in query:
            search_query = query.replace('search on google of','')
            search_google(search_query.strip())
        elif 'open calculator' in query:#manually perform mathematical operation
            calculator_path = "C:\\Windows\\System32\\calc.exe"
            os.startfile(calculator_path)
        elif 'perform mathematical operations' in query:#performs Mathematical operation according to speech
            speak("Sure! Please provide the first number.")
            while True:
                try:
                    num1 = int(takeCommand().replace(" ", ""))
                    break
                except ValueError:
                    speak("Sorry, I didn't recognize the number. Please say the number again.")

            speak("Great! Now, please provide the second number.")
            while True:
                try:
                    num2 = int(takeCommand().replace(" ", ""))
                    break
                except ValueError:
                    speak("Sorry, I didn't recognize the number. Please say the number again.")

            speak("Now, specify the operation (add, subtract, multiply, divide).")
            operation = takeCommand().lower()

            operators = {'add': '+', 'subtract': '-', 'multiply': '*', 'divide': '/'}

            if operation in operators:
                expression = f"{num1} {operators[operation]} {num2}"
                try:
                    result = eval(expression)
                    speak(f"The result of {expression} is {result}")
                    print(f"The result of {expression} is {result}")
                except Exception as e:
                    speak(f"Sorry, I couldn't perform the calculation. Error: {e}")
            else:
                speak("Sorry, I didn't recognize the operation. Please specify add, subtract, multiply, or divide.")

        elif 'jarvis quit' in query or 'stop jarvis' in query:
            speak("Jarvis Quiting The Program.....Thank You!")
            break
