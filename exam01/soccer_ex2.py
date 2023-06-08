# soccer_ex2.py

import openai
import random

# OpenAI API 설정
openai.api_key = ''


def generate_soccer_prediction(home_team, away_team):
    prompt = f"Prediction: {home_team} vs {away_team}"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=14,
        temperature=random.uniform(0.2, 0.8),
        # top_p=1.0,
        n=1,
        stop=None
    )
    generated_text = response.choices[0].text.strip()

    print(f'The predicted result : ' , response) 

    # 결과에 가능성(확률) 추가
    # confidence = round(response.choices[0].probability * 100, 2)
    # prediction_with_confidence = f"{generated_text} ({confidence}% confidence)"

    return generated_text

# 예상할 경기 팀 설정
home_team = '이탈리아'
away_team = '대한민국'

# 축구 예상 결과 생성
prediction = generate_soccer_prediction(home_team, away_team)

# 이탈리아 또는 대한민국으로만 답변하도록 수정
while prediction != home_team and prediction != away_team :
    prediction = generate_soccer_prediction(home_team, away_team)


print(f" {home_team} vs {away_team} : {prediction}")





