# exam04.py

import openai

# OpenAI API 키 설정
openai.api_key = ''

# ChatGPT에 대화 입력 및 응답 요청 함수
def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        echo=True
    )
    return response.choices[0].text.strip()

# ChatGPT와의 대화 시작
print("ChatGPT와 대화를 시작합니다. 대화를 종료하려면 'q'를 입력하세요.")

while True:
    user_input = input("사용자: ")
    if user_input.lower() == 'q':
        break
    
    # ChatGPT에 대화 입력 및 응답 받기
    prompt = f"사용자: {user_input}\nChatGPT:"
    response = chat_with_gpt(prompt)
    
    print("ChatGPT:", response)
