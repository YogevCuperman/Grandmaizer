import VoiceRecognition as voice
import Verifications
from Profile import Profile

p = Profile()

# Greetings -> getting name and id
voice.say("Hello, my name is Grandmizer.")
voice.say("What is your name?")
name = voice.listen()
while name is None:
    voice.say_again()
    name = voice.listen()
p.set_name(name)
voice.say(f"Hello {p.get_name()}, how old are you?")