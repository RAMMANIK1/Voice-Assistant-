import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser as wb
import os
import pywhatkit
import smtplib
from playsound import playsound
import pyjokes
import random


reply_nice = ('You are welcome .',
            "Ohh , It's Okay .",
            "Thanks To You.")


reply_how = ('I Am Fine.',
            "Excellent .",
            "Absolutely Fine.",
            "I'm Fine.",
            "Thanks For Asking.")



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

hot_word='hello buddy'

def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning!, Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!,Sir")   

    else:
        speak("Good Evening!,Sir")  

    speak("I am at your service.")       

def takeCommand():
    # takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.energy_threshold=4000
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query

def date():
    day=int(datetime.datetime.now().day)
    month=int(datetime.datetime.now().month)
    year=int(datetime.datetime.now().year)
    speak("The current date is")
    speak(day)
    speak(month)
    speak(year)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jyotirammanik@gmail.com', 'password of the provided email')
    server.sendmail('jyotirammanik@gmail.com', to, content)
    server.close()

def searchgoogle():
    speak("What should i search sir")
    search=takeCommand()
    wb.open('https://www.google.com/search?q='+search)

def Whatsapp():
    speak("Ok Sir tell me the person name")
    name=takeCommand()
    if 'father' in name:
        speak("Tell me the message sir")
        message=takeCommand()
        speak("Sending the message .....")
        pywhatkit.sendwhatmsg("+919937865611",message,18,39,15)
        speak("Message sent sir")
    
if __name__ == "__main__":
    clear = lambda:os.system('cls')
    clear()
    query = takeCommand().lower()
    wishMe()
    while query==hot_word:
    # if 1:
        
        asked = takeCommand().lower()
        #Logic for executing tasks based on query
       
        if 'wikipedia' in asked:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(asked, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'introduce yourself' in asked:
            speak("Hello")
            speak("Nice meeting you all ")
            speak("I am your Personal Voice assistant. \n I am developed by Jyotiram Manik,\n Pabitra Nayak \n and Jogobrata Manik")
            speak("I can perform various activities such as play music \n opening various files and webpages \nas well and many more")
            speak("How may i help you....")

        elif 'date' in asked:
            date()

        elif 'open youtube' in asked:
            speak("Opening youtube...")
            wb.open("youtube.com")
       
        elif "good morning buddy" in asked:
            speak("good morning")
            speak("How may i help you sir?")
       
        elif 'open google' in asked:
            speak("Opening google...")
            wb.open("google.com")

        
        elif 'open stack overflow' in asked:
            speak("Launching stackoverflow... Happy coding")
            wb.open("stackoverflow.com")   


        elif 'the time' in asked:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the current time is {strTime}")

        elif 'open code' in asked:
            speak("Opening vs code...")
            codePath = "C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)
        
        elif'youtube' in asked:
            asked=asked.replace("youtube search","")
            web="https://www.youtube.com/results?search_query=" + asked
            speak("Done sir!")
            wb.open(web)

        elif 'email to jyoti' in asked:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "jyotirammanik@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email") 
                break
        
        elif 'search in google' in asked:
            searchgoogle()
        
        elif 'exit' in asked:
            speak("It was nice talking you.\t Good bye sir")
            break

        elif 'play my song' in asked:
            speak('Ok Playing your song. Enjoy sir')
            playsound("C:\\Users\\HP\\Downloads\\Akhiyaan-Mitraz(PagalWorldl).mp3")
        
        elif 'play music' in asked:
            speak("What should i play sir?")
            musicname=takeCommand()
            pywhatkit.playonyt(musicname)
            speak("Your song has been started\n Enjoy Sir!")

        elif 'joke' in asked:
            speak(pyjokes.get_joke())
            speak("")
            speak("Hope you like that one sir!")
        
        elif 'website' in asked:
            speak("Sir name of the website? ")
            web1=takeCommand()
            web2='https://www.' + web1 + '.com'
            wb.open(web2)
            speak("Your website has been opened.")
        
        elif 'whatsapp' in asked:
            Whatsapp()

        elif 'folder' in asked:
            speak("Which folder you want to open sir?")
            fol=takeCommand()
            if 'SQL developer' in fol:
                os.startfile("C:\\Users\\HP\\Desktop\\sqldeveloper - Shortcut.lnk")
                speak("SQL Developer has started. Happy Coding! ")
            elif 'PowerPoint presentation' in fol:
                os.startfile("C:\\Users\\HP\\Desktop\\New Microsoft PowerPoint Presentation.pptx")
                speak("Power Point Presentation has been opened.")
            elif 'Notepad Plus' in fol:
                os.startfile("C:\\Users\\Public\\Desktop\\Notepad++.lnk")
                speak("Your code editior Notepad plue has been started.")
            elif 'Adobe Reader' in fol:
                os.startfile("C:\\Users\\Public\\Desktop\\Adobe Reader XI.lnk")
                speak("Abdob Reader has started.")
            

        elif "how " in asked:

            reply_ = random.choice(reply_how)

            speak(reply_)
        
        elif "nice"  in asked:
            reply_1=random.choice(reply_nice)
            speak(reply_1)
        
        else:
            speak("Sorry sir i am unable to perform the task assigned\nHope in near future i will be able to do\nSorry for the inconvinience.")