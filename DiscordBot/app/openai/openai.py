from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def gptResponse(prompt):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=5,
        stop=None,
        temperature=0.7,
        top_p=1,
    )
    return response.choices[0].text.strip()