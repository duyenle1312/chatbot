import speech_recognition as sr #pip install speechrecognition + PyAudio (manual downloading, coppy file name to install)
import pyttsx3 #pip install pyttsx3
from datetime import date, datetime #pip install datetime
import wikipedia

# Initializing 
robot_ear = sr.Recognizer()
robot_speak = pyttsx3.init()
robot_speak.setProperty('rate', 180) 
robot_speak.setProperty('voice', 'com.apple.speech.synthesis.voice.Alex')  #changing index, changes voices. o for male
robot_speak.say("I'm listening")
robot_speak.runAndWait()

while True:

    # Listen part
    with sr.Microphone() as source:
        print("Robot: I'm listening...")
        audio = robot_ear.listen(source, timeout=3, phrase_time_limit=3)
        #audio = robot_ear.record(source, duration=3)

    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = "..."

    print("You: " + you)

    # AI part
    robot_brain = ""
    if you == "...":
        robot_brain = "I can't hear you, try again"
    elif you == "hello":
        robot_brain = "Hello Duyen beautiful!"
    elif you == "who are you":
        robot_brain = "I'm your virtual assitant, created by Duyen."
    elif you == "today":
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif you == "time":
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "who is" in you:
    	wiki = you[7:]
    	print(wiki)
    	try:
    		robot_brain = wikipedia.summary(wiki, sentences=1, auto_suggest=False)
    	except: 
    		robot_brain = "Page not found on Wikipedia"
    elif 'bye' in you:
        robot_brain = "Bye, Duyen! See you soon!"
        print("Robot: " + robot_brain)
        robot_speak.say(robot_brain)
        robot_speak.runAndWait()
        break
    else:
        robot_brain = "Sorry, I have not been trained for this answer."

    # Speaking part
    print("Robot: " + robot_brain)
    robot_speak.say(robot_brain)
    robot_speak.runAndWait()