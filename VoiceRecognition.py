import speech_recognition
import pyttsx3
import pyaudio

recognizer = speech_recognition.Recognizer()
tts = pyttsx3.init()

say_again = "i didn't catch that. can you say that again please?"

keywords = {"can't read": "do you want me to enlarge the text?",
            "my name is": "hello, my name is Grandmizer"}


def listen():
    global recognizer
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.1)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio).lower()
            return text
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
        return say_again


def say(response):
    tts.say(response)
    tts.runAndWait()


def get_response(question):
    for kw in keywords:
        if kw in question:
            return keywords[kw]
    return "I don't know"


class Profile:
    def __init__(self):
        self.name = None
        self.cant_read = None


# MAIN LOOP

profile = Profile()

while True:
    question = listen()
    if question == say_again:
        say(say_again)
        continue
    else:
        answer = get_response(question)
        say(answer)
