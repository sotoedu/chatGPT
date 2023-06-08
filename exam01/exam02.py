#exam02.py

import os
import openai

# from dotenv import load_dotenv

# load_dotenv()

API_KEY = ''
openai.api_key = API_KEY

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="안녕하세요. 저의 이름은 소토입니다. \n\nQ: 당신의 이름은?\nA:",
  temperature=0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\n"]
)

print(response)

print(response.choices[0].text.strip())
