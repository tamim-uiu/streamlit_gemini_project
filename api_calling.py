from google import genai
from dotenv import load_dotenv
import os,io
from gtts import gTTS

#this is required because we have to convert the image in a type then give it to api
from PIL import Image

#load the env varbiable

load_dotenv()
my_api_key=os.getenv("Gemini_Api_Key")

#create client because we cant directly connect with api

client=genai.Client(api_key=my_api_key)

#create function to generate note
def note_generator(images):
    prompt="summarize the picture in note at max 50 words"
    response=client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images,prompt]
    )
    return response.text


# function for audio generate

def audio_transcription(text):
    speech = gTTS(text,lang='bn',slow=False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer

#function for quiz 
def quiz_generator(image,difficulty):

    prompt = f"Generate 3 quizzes based on the {difficulty}. Make sure to add markdown to differentiate the options. Add correct answer too,after the quiz"


    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents=[image,prompt]
    )

    return response.text 