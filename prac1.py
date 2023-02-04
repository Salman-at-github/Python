import requests
import json
from win32com.client import Dispatch

def speak(str):
    speak = Dispatch('SAPI.SpVoice')
    speak.Speak(str)
    
speak('Hello there how are you')
if __name__ == "__main__":
    apikey = input("Enter your API key: ")
    url = f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={apikey}"
    news = requests.get(url).text
    news_dict = json.loads(news)
    news_articles = news_dict['articles']
    i = 1
    speak("News headlines for today are: ")
    for article in news_articles:
        headline = article['title']
        if i != 10:
            speak(f"Headline {i} is {headline} ")
            i+=1
        else:
            speak(f"At last Headline {i} is {headline}")