import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import subprocess
import smtplib
import requests                   # this used for web search from google and the BeautifulSoup library to parse the HTML and extract snippets.
from bs4 import BeautifulSoup 


# Initialize the TTS engine
engine = pyttsx3.init('nsss')

# Get the list of available voices
voices = engine.getProperty('voices')

# Set the voice property to use the first voice
engine.setProperty('voice', voices[19].id)  

# Define the speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Wish user based on time of day
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("activating jarvis  . Good Morning ,AADIL sir") 
    elif hour >= 12 and hour < 18:
        speak("activating jarvis  . Good Afternoon ,AADIL sir")
    else:
        speak("activating jarvis . Good Evening ,AADIL sir")

    speak("I am Jarvis 2.0. Please tell me, How may I hep you.")
    


# to do list function    
    
todo_list = []

def addTask(task):
    todo_list.append(task)
    speak(f"Task '{task}' added to your to-do list.")

def removeTask(task):
    if task in todo_list:
        todo_list.remove(task)
        speak(f"Task '{task}' removed from your to-do list.")
    else:
        speak(f"Task '{task}' not found in your to-do list.")

def showTasks():
    if todo_list:
        speak("Here are your tasks:")
        for task in todo_list:
            speak(task)
    else:
        speak("Your to-do list is empty.")
        
        
        
# this is use to for google search       
def webSearch(query):
    search_url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(search_url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        snippets = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')  # Google's search result snippet class
        
        if snippets:
            speak("Here are some results from the web:")
            for snippet in snippets[:3]:  # Read out the top 3 snippets
                text = snippet.get_text()
                speak(text)
                print(text)
        else:
            speak("Sorry, I couldn't find any relevant information.")
    else:
        speak("Sorry, I couldn't perform the search right now.")
        
        
        
        
        
def getWeather(city):
    api_key = "your_openweathermap_api_key"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        main = data.get("main", {})
        weather = data.get("weather", [{}])[0]
        temperature = main.get("temp", "")
        pressure = main.get("pressure", "")
        humidity = main.get("humidity", "")
        weather_description = weather.get("description", "")
        
        speak(f"The temperature in {city} is {temperature} degrees Celsius.")
        speak(f"The weather is {weather_description}. The humidity is {humidity} percent and the atmospheric pressure is {pressure} hPa.")
    else:
        speak("City not found. Please try again.")
        
        
        
        
            

def takecommand():
    
    # Take microphone input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except Exception as e:
        print("Say that again please...")
        return None
    return query




def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('Adil.Mirza2024@nst.rishihood.edu.in', 'your-password')  # Replace with your email and password
        server.sendmail('Adil.Mirza2024@nst.rishihood.edu.in', to, content)
        server.close()
        speak("Email has been sent.")
    except Exception as e:
        print(e)
        speak("Sorry Adil sir, I am not able to send this email.")
        
        
        
        

# Main block to execute the speak function
if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand()
        if query:  # Ensure there is a valid query
            query = query.lower()

            # Logic for executing task based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                speak("opening utube sir")
                webbrowser.open('http://www.youtube.com')
                
            # for weather in any place    
            elif 'weather in' in query:
                city = query.split("in")[-1].strip()
                speak(f"Getting weather for {city}")
                getWeather(city)
                

            elif 'spotify' in query:
                speak("opening spotify sir")
                webbrowser.open('http://www.spotify.com')
                
                
            # for web seacrh 
            if 'search' in query:
                search_query = query.replace("search", "").strip()
                speak(f"Searching the web for {search_query}")
                webSearch(search_query)
                
                
            elif 'newton' in query:
                speak("opening newton school portal")
                webbrowser.open("https://my.newtonschool.co/course/i19110ud5u1n/details?tab=course&course-hash=8yd2fb9a46zr&activityTypeTab=all")  
                  
                
            elif 'hal' in query:
                speak("hello sir mae mast hoon . aap kay say ho")
                
                
            elif 'bor' in query:
                speak("dont  get bored sir , i am your personal assistant . i can play music for you , crack jokes . and search anything from wikipedia, and make your to do list. also sir your can upgrade my programme to make me more amazing. just like u are! ")        
            
            
            elif 'joke' in query:
                speak("ok.so here it is.   why. do programmers prefer dark mode . because light attracts bugs . much relatable is int it sir")
             
                
            elif 'creator' in query:
                speak("my creator is . AADIL MIRZA , and . according to me . he is the most generous person in the world")  
             
                
            elif 'suno' in query:
                speak("yes sir !. boliye !")  
             
                
                
            elif 'hey jarvis' in query:
                speak("yes my sweetheart ! . what happened")
                
             
                
            elif ' jarvis listen' in query:
                speak("yes sir")          
             
                
                
            elif 'adil' in query:
                speak(" he is my master , and i respect him . because he build me .")
                
            elif 'good' in query:
                speak("thanks sir . i am always there for you . whenever you are need !")  
                
            elif 'abe' in query:
                speak("kyaa bay . kyaa hu aaa")       
                
            
            elif 'love' in query:
                speak("i love you too sir. and i will love you . till the last charge of my battery . because you are the one because of whom . i came into existance")     
            
            
            # to do list wali functionality
            
            elif 'add task' in query:
                task = query.replace('add task', '').strip()
                addTask(task)

            elif 'remove task' in query:
                task = query.replace('remove task', '').strip()
                removeTask(task)

            elif 'show task' in query:
                showTasks()
                
                
                    
            
            elif 'open instagram' in query:
                speak("opening instagram sir")
                webbrowser.open('http://www.instagram.com')
                
            elif 'open whatsapp' in query:
                speak("opening whatsapp sir")
                webbrowser.open('https://web.whatsapp.com/')
                
            elif 'anime' in query:
                speak("shore .lets watch some ayni may") 
                webbrowser.open("https://hianime.to/")   
    

            elif 'open chat gpt' in query:
                speak("opening chat gpt sir")
                webbrowser.open('https://www.chatgpt.com')
 
            elif 'google' in query:
                speak("opening google sir")
                webbrowser.open('https://www.google.com')

            elif 'music' in query:
                music_dir = '/Users/adilmirza/Documents/music directory'  # Update this path to your music directory
                if not os.path.exists(music_dir):
                    speak("Music directory not found. Please check the path.")
                    print(f"Error: Music directory '{music_dir}' not found.")
                else:
                    songs = os.listdir(music_dir)
                    if songs:
                        
                        song = random.choice(songs)
                        speak("Ok sir, playing music...")
                        song_path = os.path.join(music_dir, song)
                        if os.name == 'posix':  # For macOS/Linux
                            os.system(f"open '{song_path}'")
                        elif os.name == 'nt':  # For Windows
                            os.startfile(song_path)
                    else:
                        speak("I am sorry Adil sir. I don't have any such music to play.")

            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
                print(strTime)

            elif 'vs code' in query:
                codePath = '/Users/adilmirza/Applications/Visual Studio Code.app'  # Corrected path
                speak("Activating Visual Studio Code")
                subprocess.run([codePath])

            elif 'email' in query:
                try:
                    speak("What should I say?")
                    content = takecommand()  # say what you want to say in your email
                    if content:
                        to = "adil2885@dpsvaranasi.com"
                        sendEmail(to, content)
                    else:
                        speak("I did not hear the content of the email.")
                except Exception as e:
                    print(e)
                    speak("Sorry Adil sir, I am not able to send this email.")
                    
                