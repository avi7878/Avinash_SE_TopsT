import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 130)  
engine.setProperty('volume', 4) 

engine.say("Hello Avinash")
voice = input("Type you speak : ")

engine.say(voice)
engine.save_to_file(voice,"voice.mp3")
engine.runAndWait()
