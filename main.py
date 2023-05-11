import VoiceRecognition as voice
import Verifications
from Profile import Profile
import Classifier

p = Profile()

# Greetings -> getting name and id
voice.say("Hello, my name is Grandmizer.")
voice.say("What is your id?")
id = voice.listen()
while id is None:
    voice.say_again()
    id = voice.listen()
p.set_id_number(id)
voice.say(f"Hello, what is your problem?")
problem = voice.listen()
while problem is None:
    voice.say_again()
    problem = voice.listen()
    p.set_problem(problem)
get_response = Classifier.get_response(problem)
voice.say(get_response)
