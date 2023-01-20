#  make a ai virtual assistant
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import pyautogui
import pyperclip
import psutil
import pyjokes
import requests
import json
import wolframalpha
import pywhatkit
import subprocess
import PyPDF2
import winshell
import time
import tkinter as tk
from tkinter import PhotoImage
root = tk.Tk()
root.configure(bg="black")
root.geometry("800x600")

# Add a label for displaying the output
output_label = tk.Label(root, text="Output:", font=("Arial", 14), fg="white", bg="black")
output_label.pack()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
#  wish me function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you")

# take command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        output_label.config(text=query) # update the output label with the query
    except Exception as e:
        print("Say that again please...")  
        output_label.config(text="Say that again please...") # update the output label with error message
        return "None"
    return query


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    speak("Sir, what should i do for you")
    output_label.config(text='CPU usage: ' + usage + '%')

def screenshot():
    img = pyautogui.screenshot()
    img.save("ss.png")
    output_label.config(text='Screenshot taken and saved as ss.png')  
            
def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('youremail@gmail.com', 'your-password')
        server.sendmail('youremail@gmail.com', to, content)
        server.close()
        output_label.config(text='Email sent successfully')
    except:
        output_label.config(text='Failed to send email')
    
if __name__ == "__main__":
    wishMe()
if __name__ == "__main__":
    wishMe()
    # Create button for 'cpu' functionality
    # Create button for 'screenshot' functionality
            screenshot_button = tk.Button(root, text="Screenshot", font=("Arial", 14), fg="white", bg="black", command=screenshot)
      screenshot_button.pack()
      # Create button for 'email' functionality
      email_button = tk.Button(root, text="Email", font=("Arial", 14), fg="white", bg="black", command=lambda: sendEmail("to_email@example.com", "Email content"))
      email_button.pack()
      # Create button for 'exit' functionality
      exit_button = tk.Button(root, text="Exit", font=("Arial", 14), fg="white", bg="black", command=root.destroy)
      exit_button.pack()
      root.mainloop()
    while True:
    # if 1:
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
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        elif 'open code' in query:
            codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif 'email to rahul' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "arjavchoudhary608@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend arjav. I am not able to send this email")
                
        elif 'quit' in query:
            exit()
            
        elif 'exit' in query:
            exit()
            
        elif 'remember that' in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("You said me to remember that" + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
            
        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("You said me to remember that" + remember.read())
            
        elif 'screenshot' in query:
            screenshot()
            speak("Done!")
            
        elif 'cpu' in query:
            cpu()
            
        elif 'joke' in query:
            speak(pyjokes.get_joke())
            
        elif 'go offline' in query:
            speak("Going offline sir")
            quit()
            
        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing' + song)
            pywhatkit.playonyt(song)
            
        elif 'who i am' in query:
            speak("If you talk then definately your human.")
            
        elif 'why you came to world' in query:
            speak("Thanks to arjav. further It's a secret")
            
        elif 'who are you' in query:
            speak("I am your virtual assistant created by arjav")
            
        elif 'are you single' in query:
            speak("I am in a relationship with wifi")
            
        elif 'i love you' in query:
            speak("It's hard to understand")
            
        elif 'what is' in query:
            question = query.replace('what is', '')
            answer = wikipedia.summary(question, 1)
            speak(answer)
            
        elif 'who is' in query:
            question = query.replace('who is', '')
            answer = wikipedia.summary(question, 1)
            speak(answer)
            
        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister arjav ")
            
        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "Location of wallpaper", 0)
            speak("Background changed succesfully")
            
        elif 'news' in query:
            try:
                jsonObj = urlopen("http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=your-api-key")
                data = json.load(jsonObj)
                i = 1
                
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                
                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                print(str(e))
                
        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open(query)
            
        elif 'ask' in query:
            speak('I can answer to computational and geographical questions too just try me!! what do you want to ask')
            question = takeCommand()
            app_id = "Your unique ID"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
            
        elif 'log off' in query or 'sign out' in query:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
            
        elif 'shutdown' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')
            
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
            
        elif 'stop listening' in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
            
        elif 'restart' in query:
            subprocess.call(["shutdown", "/r"])
            
        elif 'hibernate' in query or 'sleep' in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
            
        elif 'write a note' in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
                
        elif 'show note' in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))
            
        elif 'update assistant' in query:
            speak("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream = True)
            
            with open("Voice.py", "wb") as Pypdf:
                total_length = int(r.headers.get('content-length'))
                for ch in progress.bar(r.iter_content(chunk_size = 2391975),
                                       expected_size =(total_length / 1024) + 1):
                    if ch:
                        Pypdf.write(ch)
                        
        elif 'where is' in query:
            query = query.replace("where is", "")
            
        elif 'calculate' in query:
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)
            
        elif 'increase volume' in query:
            speak("What should i increase the volume by")
            vol = takeCommand()
            vol = int(vol)
            pyautogui.press('volumeup', presses = vol)
            
        elif 'decrease volume' in query:
            speak("What should i decrease the volume by")
            vol = takeCommand()
            vol = int(vol)
            pyautogui.press('volumedown', presses = vol)
            
        elif 'mute volume' in query:
            pyautogui.press('volumemute')
            
        elif 'take backup' in query:
            source = 'C:\\Users\\arjav\\Desktop\\jarvis'
            destination = 'E:\\Backup'
            files = os.listdir(source)
            for f in files:
                sutil.copy((source + f), destination)
                
        elif 'speak the pdf' in query:
            speak("What is the name of the file")
            name = takeCommand()
            book = open(name, 'rb')
            pdfReader = PyPDF2.PdfFileReader(book)
            pages = pdfReader.numPages
            speak("Sir, The number of pages in the book are")
            speak(pages)
            speak("Sir, Please enter the page number i have to read")
            pg = int(takeCommand())
            page = pdfReader.getPage(pg)
            text = page.extractText()
            speak(text)            
