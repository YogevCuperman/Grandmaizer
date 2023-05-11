import VoiceRecognition as voice
import Verifications
from Profile import Profile
import Classifier

p = Profile()
problem_solved = False

# voice.say("Hello, my name is Grandmeizer.")
# voice.say("What is your id?")
# id = voice.listen()
# while id is None or not Verifications.id_check(id):
#     voice.say_again()
#     id = voice.listen()
# p.set_id_number(id)
voice.say(f"Hello, what is your problem?")
problem = voice.listen()
while problem is None:
    voice.say_again()
    problem = voice.listen()
# problem = "i lost my credit card"
response = Classifier.get_response(f"You are a customer-service representative "
                                   f"of a credit card company and you are supposed to solve my problem: {problem}. "
                                   f"You can ask me one question at a time to fill in the information you need. Do "
                                   f"not answer yourself. Do not finish without a "
                                   f"question or an helpful and pragmatic answer. After giving an answer "
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

