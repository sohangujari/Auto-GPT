from API import *

import google.generativeai as genai

try:
    genai.configure(api_key=gemini_api)
except KeyError:
    print("Error: 'api_key' environment variable not found.")

model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat()

response = chat.send_message('Hello')

print(response.text)
