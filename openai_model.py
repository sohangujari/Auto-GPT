from API import *

import openai

openai.api_key = openai_api

query = "Hello"

def gpt(tprompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": tprompt}
        ],
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response.choices[0].message['content'])

gpt(tprompt=f"User: {query.lower()}\n AutoGPT: ")
