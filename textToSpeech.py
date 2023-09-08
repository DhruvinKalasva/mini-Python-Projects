import pyttsx3


data = input("Enter the text which you want to convert into speech: \n ")

engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()