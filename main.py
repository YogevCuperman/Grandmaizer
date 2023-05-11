import VoiceRecognition as voice
import Verifications
from Profile import Profile
import Classifier

p = Profile()
Classifier.reset()
problem_solved = False

# voice.say("Hello, my name is Grandmayzer.")
#
# voice.say("What is your name?")
# name = voice.listen()
# while name is None:
#     voice.say_again()
#     name = voice.listen()
# p.set_name(name)
#
# voice.say(f"Hello {name}, how old are you?")
# age = voice.listen()
# while age is None:
#     voice.say_again()
#     age = voice.listen()
# p.set_age(int(age))
#
# voice.say("What is your id?")
# id = voice.listen()
# while id is None or not Verifications.id_check(id):
#     if id is None:
#         voice.say_again()
#     else:
#         voice.say("Invalid identification number. Please try again.")
#     id = voice.listen()
# p.set_id_number(id)

voice.say("What is the issue you are experiencing?")
problem = voice.listen()
while problem is None:
    voice.say_again()
    problem = voice.listen()

response = Classifier.get_response(f"You are an actor in the following scenario: You are a customer-service "
                                   f"representative "
                                   f"of a credit card company and you are supposed to solve my problem: {problem}. "
                                   f"You can ask me one question at a time to fill in the information you need. Do "
                                   f"not answer yourself. After giving an answer "
                                   f"(which is not a question you ask), check if the problem is solved."
                                   f"Do not mention the roles in the conversation and dont write any of the"
                                   f"customer lines. When you finish the conversation say 'Would you like "
                                   f"to talk with a real person?' without any other words.")

while not problem_solved:
    voice.say(response)
    client = voice.listen()
    while client is None:
        voice.say_again()
        client = voice.listen()
    response = Classifier.get_response(client)
    if 'Would you like to talk with a real person?' in response:
        client = voice.listen()
        while client is None:
            voice.say_again()
            client = voice.listen()
        if 'no' in client:
            problem_solved = True

print('CONVERSATION ENDED')

