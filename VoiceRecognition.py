import speech_recognition
import pyttsx3
import pyaudio

recognizer = speech_recognition.Recognizer()
tts = pyttsx3.init()

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
        return None


def say(response):
    tts.say(response)
    tts.runAndWait()

def say_again():
    say("i didn't catch that. can you say that again please?")
