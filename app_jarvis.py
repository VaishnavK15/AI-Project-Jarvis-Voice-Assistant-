import streamlit as st
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import subprocess
import pyttsx3

# Streamlit UI Config
st.set_page_config(page_title="Jarvis AI", layout="centered")
st.markdown("""
    <h1 style='text-align: center; color: cyan;'>🤖 Jarvis AI Assistant</h1>
    <hr style='border: 1px solid gray;'>
    """, unsafe_allow_html=True)

# Global function for voice output
def speak(text):
    try:
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        st.error(f"Error in speaking: {e}")

# Greeting function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        greeting = "Good Morning"
    elif hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"
    speak(greeting)
    speak("Jarvis Here! How may I help you sir?")
    return greeting + "! Jarvis at your service."

# About function
def AboutJarvis():
    info = (
        "Hello I Am Jarvis AI!\n"
        "Built Using Python Programming Language By Vaishnav Kokate.\n"
        "Speed One Terahertz.\n"
        "Memory Capacity One Zettabyte.\n"
        "You Can Use Me For Automation of your device... Thank You!"
    )
    speak(info)
    return info

# Command processor
def processCommand(query):
    response = ""
    try:
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            response = results

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")
            response = "Opening YouTube"

        elif 'open google' in query:
            webbrowser.open("https://google.com")
            response = "Opening Google"

        elif 'open gpt' in query:
            webbrowser.open("https://chat.openai.com")
            response = "Opening ChatGPT"

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Vaishnav T Kokate\\OneDrive\\Desktop\\songs'
            songs = os.listdir(music_dir)
            song = random.choice(songs)
            os.startfile(os.path.join(music_dir, song))
            response = f"Playing music: {song}"

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            response = f"The time is {strTime}"

        elif 'open vs code' in query:
            code_path = "C:\\Users\\Vaishnav T Kokate\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            subprocess.Popen(code_path)
            response = "Opening Visual Studio Code"

        elif 'tell me about you' in query:
            response = AboutJarvis()

        elif 'search on google for' in query:
            search_query = query.replace('search on google for', '')
            search_url = f"https://www.google.com/search?q={search_query.strip()}"
            webbrowser.open(search_url)
            response = f"Searching Google for {search_query.strip()}"

        elif 'open calculator' in query:
            os.startfile("C:\\Windows\\System32\\calc.exe")
            response = "Opening Calculator"

        elif 'jarvis quit' in query or 'stop jarvis' in query:
            response = "Jarvis quitting. Thank you!"
            speak(response)
            st.stop()

        else:
            response = "Sorry, I did not understand the command."

    except Exception as e:
        response = f"Error while processing: {e}"

    speak(response)
    return response

# Voice command input
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Listening...")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        return query
    except:
        return "None"

# UI Buttons
if st.button("🎙️ Activate Jarvis"):
    greeting = wishMe()
    st.success(greeting)

if st.button("🧠 Give Command by Voice"):
    user_query = takeCommand().lower()
    st.write(f"You said: **{user_query}**")
    if user_query != "None":
        response = processCommand(user_query)
        st.success(f"Jarvis: {response}")
    else:
        st.warning("Could not recognize speech. Please try again.")