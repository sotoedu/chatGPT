# soccer_ex1.py

import openai

# OpenAI API 설정
openai.api_key = ''

def generate_soccer_prediction(home_team, away_team):
    prompt = f"Prediction: {home_team} vs {away_team}"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
        top_p=1.0,
        n=1,
        stop=None
    )
    generated_text = response.choices[0].text.strip()
    return generated_text

# 예상할 경기 팀 설정
home_team = '이탈리아'
away_team = '한국'

# 축구 예상 결과 생성
prediction = generate_soccer_prediction(home_team, away_team)
print(prediction)
