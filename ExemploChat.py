import openai
import json
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

client = openai.Client()

mensagens = [{'role': 'user', 'content' : 'o que é um celular?'}]

responsta = client.chat.completions.create(
  messages=mensagens,
  model='gpt-3.5-turbo-0125',
  max_tokens=1000,
  temperature=0
)

print(responsta.choices[0].message.content)