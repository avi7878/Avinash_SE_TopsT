import speech_recognition as s 
ac = s.Recognizer()
with s.Microphone() as m:
    audio = ac.listen(m)
    
    query = ac.recognize_google(audio,language='eng-in')
    print(query)



# import speech_recognition as sr

# Create a recognizer object
# recognizer = sr.Recognizer()

# Use the default microphone as the audio source
# with sr.Microphone() as source:
#     print("Speak something...")
#     audio = recognizer.listen(source)

    # try:
    #     # Recognize speech using Google Speech Recognition
    #     text = recognizer.recognize_google(audio)
    #     print("You said: " + text)
    # except sr.UnknownValueError:
    #     print("Sorry, I could not understand your speech.")
    # except sr.RequestError as e:
    #     print("Could not request results from Google Speech Recognition service; {0}".format(e))
