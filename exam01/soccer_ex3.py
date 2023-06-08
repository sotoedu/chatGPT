# soccer_ex3.py

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
        n=10,
        # log_level="info"
    )
    predictions = [choice.text.strip() for choice in response.choices]

    print(f'The predicted result : ' , predictions ) 
    
    # 이탈리아와 대한민국 결과의 비율을 조절하여 적절하게 출력
    italy_count = predictions.count(home_team)
    korea_count = predictions.count(away_team)

    print(f'italy_count : ' , italy_count ) 
    print(f'korea_count : ' , korea_count ) 
    
    if italy_count > korea_count:
        predictions = [pred if pred != home_team else away_team for pred in predictions]
        print(f'italy_count : ' , predictions )
    elif korea_count > italy_count:
        predictions = [pred if pred != away_team else home_team for pred in predictions]
        print(f'korea_count : ' , predictions )

    return random.choice(predictions)

# 예상할 경기 팀 설정
home_team = '이탈리아'
away_team = '대한민국'

# 축구 예상 결과 생성
prediction = generate_soccer_prediction(home_team, away_team)

print(f" {home_team} vs {away_team} : {prediction}")
