# ex2.py

import openai

API_KEY = ''
openai.api_key = API_KEY

prompt= '''How big is the moon?
What's the Chicago's population?

'''

response = openai.Completion.create(
    prompt = prompt,
    model = 'text-davinci-003',
    max_tokens=1000,
    temperature=0.9,
    n=3,
    stop=['---']
)

print(response)
print(response.usage.total_tokens)

for result in response.choices:
    print(result.text)
