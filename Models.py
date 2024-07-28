import openai

from API import *

# Replace "YOUR_API_KEY" with your actual OpenAI API key
# openai.api_key = ""

# query = "Write a email to elon musk"

# def gpt(tprompt):
#     response = openai.Completion.create(
#     engine="gpt-3.5-turbo",
#     prompt=tprompt,
#     temperature=0.7,
#     max_tokens=256,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0
#     )
#     print(response.choices[0].text)

# gpt(tprompt=f"User: {query.lower()}\n AutoGPT: ")


import google.generativeai as genai

try:
    genai.configure(api_key=gemini_api)
except KeyError:
    print("Error: 'api_key' environment variable not found.")

model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat()

response = chat.send_message('In one sentence, explain how a computer works to a young child.')

print(response.text)
