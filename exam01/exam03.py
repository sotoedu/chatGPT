# exam03.py

import openai
openai.api_key = ''

for _ in range(5):
    text = openai.Completion.create(
      model="text-davinci-003",
      prompt="한국에서 유명한 음식은 ",
      max_tokens=300,
      temperature=1,
      n=5,
    )

    print(text['choices'][0]['text'])
    print("==============================")
