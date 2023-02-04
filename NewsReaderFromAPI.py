import requests
import json

#myapi: f5998a1d00dc460baac86299b17958e9 



def speak(str):
    from win32com.client import Dispatch
    
    speak = Dispatch('SAPI.SpVoice')
    speak.Speak(str)
    
if __name__== "__main__":
    
    api = input("Enter your APN: ")
    url = f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={api}"
    news = requests.get(url).text            #this news is in string format, now we use json to make news string into dictionary so that we can play only the 'title' (print news to verify)
    news_dict = json.loads(news)
    
    #'articles' must exist in the news site data for it to be found, else error
    news_articles = news_dict['articles']           #we need only articles
    
    speak("Welcome to news wizard. I'll tell you the top 10 tech news headlines of today.")
    i = 1
    for article in news_articles:                              #to access only articles one by one
        #print(article['title'])                                #to access only the title and not entire article
        if i==10:
            speak(f" and at last, Headline {i} is: {article['title']}. Thank you for listening. Have a nice day.")
        else:
            speak(f"Headline {i} is: {article['title']}")
            i+=1
            
        
        
     
    
