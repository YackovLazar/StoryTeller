import os
from pyexpat.errors import messages
import openai
import dotenv

dotenv.load_dotenv('token.env')
openai.organization = os.getenv('ORG_ID')
openai.api_key = os.getenv('TOKEN_GPT')

# completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world!"}])
# print(completion.choices[0].message.content)

def get_response(question):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{"role": "user", "content": question}],
        max_tokens = 500,
        top_p = 0.1)
    return response.choices[0].message.content