#reading newspaper

import requests
import json
import time
from win32com.client import Dispatch

def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

data = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=Your API Key")

result = data.json()
print(result['status'])
# print(result)

news = result['articles']

if __name__ == "__main__":
    speak("Hello! Welcome to MX News Channel")
    speak("Here are the today's top ten news from India!")

    for i in range(0,10):
        print(i)
        print(news[i]['description'])
        speak(news[i]['description'])

        if i>= 9:
            break
        time.sleep(0.8)
        if i == 8:
            speak("So our last news for today is")
        else:
            speak("Moving To Our Next news")

speak("Thanks for listening! Have a nice day")
