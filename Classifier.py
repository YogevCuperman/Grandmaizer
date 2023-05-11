import openai

# Set your OpenAI API Key
api_key = "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"

openai.api_key = api_key


# def get_response(prompt):
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=prompt,
#         temperature=0.2,
#         max_tokens=256,
#         n=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
#     print(response.choices[0].text)
#     return response.choices[0].text

chat_log = []

def get_response(prompt):
    chat_log.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_log
    )
    assistant_response = response['choices'][0]['message']['content'].strip("\n").strip()
    chat_log.append({"role": "assistant", "content": assistant_response})
    print(assistant_response)
    return assistant_response

def reset():
    chat_log = []
