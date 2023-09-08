
import speech_recognition as sr

def getaudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("say Something to print- ")
        audio = r.listen(source)
        print("done recording!!!")

    try:
        text = r.recognize_google(audio)
        print("you said- \n" +text)

    except Exception as e:
        print(e)

getaudio()