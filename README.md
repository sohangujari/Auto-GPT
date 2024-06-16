<summary>⚠️ Note: Currently, this code will work only on Windows</summary>

# Auto-GPT 🤖

This is a virtual assistant powered by OpenAI's GPT-3 API. It can understand voice commands using speech recognition and respond via text-to-speech.

## Usage

The main.py file contains the core logic for Auto-GPT. It uses the following key libraries:

- SpeechRecognition - for speech-to-text 
- PyWin32 - for text-to-speech
- OpenAI - for generating responses with GPT-3
- Requests - for weather API calls

Auto-GPT responds to commands like:

- Open websites (YouTube, Gmail etc) 
- Play songs
- Get the current time
- Search YouTube
- Get the weather
- Have a conversation using GPT-3

It also prints what the user said and its own response.

## Setup

- Install requirements:

```
pip install -r requirements.txt
```

- Add OpenAI and weather API keys in main.py

- Run main.py

```
python main.py
```

- Talk to Auto-GPT!

## Customization

- The `sites` list contains websites that Auto-GPT can open 
- Adjust OpenAI temperature, max tokens etc to tweak GPT-3 response
- Change text-to-speech voice via win32com
- Add more skills by expanding the command handling logic

## To Do:

- Voice recognition improvements
- More intelligent conversations
- Deployable web service?
