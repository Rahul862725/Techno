import pyttsx3
import speech_recognition as src
import datetime
import wikipedia
import webbrowser
import os
# import PyAudio
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[].id)
engine.setProperty('voice',voices[0].id)
engine.setProperty('language','hi')
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<15:
        speak("Good Afternoon")
    elif(hour>=16 and hour<17):
        speak("Good Evening")
    else:
        speak("Good night")

def takeCommand(name="None"):
    r=src.Recognizer()
    with src.Microphone() as source:
        print("Listening...")
        # r.phrase_threshold=1
        audio=r.listen(source)
    try:
        print("Recongnizing...")
        query=r.recognize_google(audio,language="en-in")
        if(name!="None"):
            print(f"I am understand that {name} said: {query}")
            speak(f"I am understand that {name} said: {query}")
    except Exception as e:
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query;




if __name__=="__main__":
    speak("Hi Sir!")
    wishMe()
    speak("I am Techno, i am make for help peoples. I can do some task like search anything in google youtube, tell you about current time , open anything in wekipedia, open stackoverflow and by quite command i will stop my work. ")
    speak("This is my introduction.")
    speak("Now Please tell me What's your Beautiful name! so that more interaction can stablished between us")
    name=None;
    while(nmae==NOne):
        name=takeCommand()
        if name==None:
            speak("PLease tell me your name...")
    speak(f"ok, Now tell {name} me How can i help you!")
    while True:
        query=takeCommand(name).lower()
        if 'wikipedia' in query:
            query=query.replace("wikipedia","")
            try:
                results=wikipedia.summary(query,sentences=2)
                speak("Acording to Wikipedia")
                speak(results)
                print(results)
            except Exception as e:
                speak(f"{name} This is not find in WIkipedia. Please Say anthing else...")

        elif "your name" in query:
            speak(f"Dear {name} as i said My name is Techno. I am make for help people in working.")
        elif "you do" in query:
            speak("As i said previsouly , i am make for help peoples. I can do some task like search anything in google youtube, tell you about current time , open anything in wekipedia, open stackoverflow and by quite command i will stop my work.")
        elif "open youtube" in query:
            speak(f"What {name} want to search")
            search=takeCommand().lower()
            webbrowser.open("youtube.com/?#q="+search)
        elif "open google" in query:
            speak(f"What{name} want to search")
            search = takeCommand()
            webbrowser.open("google.com/?#q="+search)
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "time" in query:
            str=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"{name} the time is {str}")
        elif "open code" in query:
            path="C:\\Users\\UPLC\\AppData\\Local\\Programs\\Microsoft VS Code";
            os.startfile(path,open)
            os.close()
        elif "quite" in query:
            speak(f"OK {name}.I am very happy to help You.Thank you")
            # wishMe()
            break
