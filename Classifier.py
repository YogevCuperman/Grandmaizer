import openai

# Set your OpenAI API Key
api_key = "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"

openai.api_key = api_key


def get_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text
