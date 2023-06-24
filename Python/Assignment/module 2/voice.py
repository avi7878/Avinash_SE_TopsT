import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 130)  
engine.setProperty('volume', 4) 

engine.say("Thank you visit again.")


engine.runAndWait()
