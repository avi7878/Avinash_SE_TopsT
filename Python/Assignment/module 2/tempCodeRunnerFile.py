import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)  
engine.setProperty('volume', 10) 

engine.say("Thank you visit again.")


engine.runAndWait()
