# import pyttsx3
# engine = pyttsx3.init()
# engine.say("Hello world")
# engine.runAndWait()
from gtts import gTTS
import os

# # Text to be converted to speech
# text = "Hello, how are you today?"

# # Language in which you want to convert
# language = 'en'

# # Passing the text and language to the engine, here we have marked slow=False.
# # Which tells the module that the converted audio should have a high speed
# speech = gTTS(text=text, lang=language, slow=False)

# # Saving the converted audio in a mp3 file named "speech.mp3"
# speech.save("speech.mp3")

# # Playing the converted file
# os.system("start speech.mp3")  # Use "afplay speech.mp3" on macOS or "mpg321 speech.mp3" on Linux
