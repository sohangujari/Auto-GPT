import speech_recognition as sr
import pyttsx3
import webbrowser
import os
from datetime import datetime
import openai
import requests
import json

openai.api_key = "API_KEY"
wheather_api = "API_KEY"
speech = pyttsx3.init()
now = datetime.now()

speech.setProperty('rate', 150)    # Speed of speech
speech.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

def say(text):
    speech.say(text)
    speech.runAndWait()

def gpt(tprompt):
    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=tprompt,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    say(response.choices[0].text)

def takeCommand():
    reco = sr.Recognizer()
    with sr.Microphone() as source:
        reco.pause_threshold = 0.8
        reco.energy_threshold = 1000
        audio = reco.listen(source)
        try:
            query = reco.recognize_google(audio, language = "en-in")
            print(f"User: {query}")
            return query
        except Exception as e:
            return "Some error occurred. Sorry from AutoGPT"

say("Hello, I'm AutoGPT")
say("How can i help you")

while True:
    print("Listening...")
    query = str(takeCommand())

    sites = [["youtube","https://www.youtube.com/"],
            ["dribbble","https://dribbble.com/"],
            ["gmail","https://mail.google.com"],
            ["linkedin","https://www.linkedin.com/feed/"]]
    for site in sites:
        if f"open {site[0]}" in query.lower():
            webbrowser.open(site[1])
            say(f"Opening {site[0].capitalize()}...")

    if "play song" in query.lower():
        os.startfile("D:\Calm Down.mp3")
        say("Playing Song...")

    if "open photoshop" in query.lower():
        os.startfile("C:\Program Files\Adobe\Adobe Photoshop CC 2019\Photoshop.exe")
        say("Opening Photoshop...")

    if "the time" in query.lower():
        time = now.strftime("%I")
        minutes = now.strftime("%M")
        period = now.strftime("%p")
        say(f"It's {time}{minutes}{period}")
        print(f"{time}:{minutes} {period}")

    if "on youtube" in query.lower():
        text=query.lower()
        rep_text = text.replace("watch ", "").replace(" on youtube", "")
        link_text = rep_text.replace(" ","+")
        website = (f"https://www.youtube.com/results?search_query={link_text}")
        webbrowser.open(website)
        say(f"watch {rep_text}")

    if "weather" in query.lower():
        city = query.split("in ", 1)[1]
        url = f"https://api.weatherapi.com/v1/current.json?key={wheather_api}&q={city}"

        r = requests.get(url)
        weather = json.loads(r.text)
        temperature = (weather["current"]["temp_c"])
        say(f"The current weather in {city} is {temperature} degrees")

    gpt(tprompt=f"User: {query.lower()}\n AutoGPT: ")
    
    if (query.lower() == "ok bye"):
        break
