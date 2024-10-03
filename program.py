from gtts import gTTS
import google.generativeai as genai
import playsound
GOOGLE_API_KEY ="AIzaSyAHa67vfrBKnspsNztfXu1x8XqMPxYD8-s"

genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]
model = genai.GenerativeModel('gemini-1.0-pro-latest', generation_config=generation_config,safety_settings=safety_settings)

system_message = '''you are used to a power a voice assistant anf should respond 
as so. as a voice assistant , use short sentance and 
 directly respond to the prompt without excessive informatopn 
.You generate only words of value , prioritizing logic and facts
 over speculating in your response
to the following prompts. You should not generate a response more than 50 words, try to give short responses.'''
system_message.replace(f'\n',' ')
language = 'en'

convo = model.start_chat()
convo.send_message(system_message)
while True:
    user_input = input("user input : ")
    convo.send_message(user_input)
    print("GEMINI:",convo.last.text)
    tts = gTTS(text=convo.last.text,lang=language)
    tts.save("output.mp3")
    playsound.playsound("output.mp3")
