import boto3
from botocore.config import Config
import playsound
import speech_recognition as sr
import openai
import os
from contextlib import closing

openai.api_key = "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" #os.environ["OPENAI_API_KEY"]
my_config = Config(
    region_name = 'us-west-2'
)
recognizer = sr.Recognizer()
polly = boto3.client("polly", config=my_config)

def voice_to_text():
    with sr.Microphone() as source:
        print(">Please talk:")
        audio = recognizer.listen(source)
    return recognizer.recognize_whisper_api(audio, api_key=openai.api_key)

def create_text(messages):
    print("Asking ChatGPT...")
    result = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )
    response_text = result['choices'][0]['message']['content']
    return response_text

def text_to_voice(text):
    path_to_mp3 = "./voice.mp3"
    response = polly.synthesize_speech(
        Engine='neural',
        Text = text,
        OutputFormat = "mp3",
        VoiceId = "Hala"
    )
    audio_stream = response.get("AudioStream")
    if audio_stream:
        with closing(audio_stream) as stream:
            with open(path_to_mp3, "wb") as file:
                file.write(stream.read())
    playsound.playsound(path_to_mp3)

messages = []
while True:
    text = voice_to_text()
    if text == "":
        continue
    print("You:", text)
    messages.append(
        {'role': 'user', 'content': text}
    )
    response_text = create_text(messages)
    print("ChatGPT:", response_text)
    messages.append(
        {'role': 'assistant', 'content': response_text}
    )
    text_to_voice(response_text)