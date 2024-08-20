
import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
import requests
from bs4 import BeautifulSoup
import subprocess
def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        # print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing your voice...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User input: {query}\n")
            return query
        except Exception as e:
            return "Sorry I am unable to recognize your voice"

# def alaram(query):
#         timhere = open("alaram.txt", "a")
#         timehere.write(query)
#         timehere.close()
#         os.startfile("alaram.py")

query = "Your string to write to the file."
with open("alaram.txt", "a") as timehere:
    timehere.write(query)
subprocess.call(["python3", "alaram.py"])

if __name__ == "__main__":
    print('This is MARK(aplha-test)')
    say("Hey there!, I am mark")
    while True:
        print("Listing...")
        query = takeCommand()
        sites = ["Youtube", "https://www.youtube.com/"], ["Google", "https://www.google.com"], ["Microsoft", "https://www.microsoft.com"], ["Apple", "https://www.apple.com"], ["Discord", "https;//discord.com/"], ["Amazon", "https://amazon.in/"], ["Wikipedia", "https://wikipedia.com/"]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        if "open msuic" in query:
            musicPath = "your music path"
            os.system(f"opening {musicPath} sir...")
        elif "what is the time" in query:
            currTime = datetime.datetime.now().strftime("%H:%M %S")
            say(f" sir the time is {currTime}")
        elif "open factime".lower() in query.lower():
            os.system(f"open /System/Applications/FaceTime.app")
        elif "open find my".lower() in query.lower():
            os.system(f"open /System/Applications/FindMy.app")
        elif "open notes".lower() in query.lower():
            os.system(f"open /System/Applications/Notes.app")
        elif "who are you".lower() in query.lower():
            say("Hello I am mark GPT your daily to-do assistant, I can get your daily task easily done in no time, how can I help you today?")
        elif "open whatsapp".lower() in query.lower():
            os.system(f"open /System/Applications/WhatsApp.app")
        elif "tell me about your yourslef".lower() in query.lower():
            say("I am currently in development stage but I can help you get your daily task done like never before, how can I help you today?")
        elif "temprature".lower() in query.lower():
            search = "temprature in vadodara"
            url = f"https://search.brave.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "htm.parser")
            temp = data.find("div", class_ = "BNeawe").text
            say(f"current{search} is {temp}")
        elif "weather".lower() in query.lower():
            search = "weather in vadodara"
            url = f"https://search.brave.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "htm.parser")
            temp = data.find("div", class_ = "BNeawe").text
            say(f"current{search} is {temp}")
        elif "the time".lower() in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir, the time is{strTime}")
        elif "finally sleep".lower() in query.lower():
            say("Logging out of the system sir")
            exit()
