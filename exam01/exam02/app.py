#app.py

from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
# CORS(app)

API_KEY = ''

@app.route("/api/text", methods=["POST"])
def TextMassageMaker():	
    payload = request.get_json()    

    receiver = payload['receiver']
    purpose = payload['purpose']
    tone = payload['tone']
    more_info = payload['more_info']

    print('receiver : ' , receiver)
    print('purpose : ' , purpose)
    print('tone : ' , tone)
    print('more_info : ' , more_info)

    # set api key
    openai.api_key = API_KEY

    # Call the chat GPT API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
   			{"role": "system", "content": "너는 문자를 작성하는 문자 마법사이다. 조건에 맞게 문자를 최대한 길게 작성하라."},
            {"role": "system", "content": "문자의 시작은 '안녕하세요'로 한다\n- 도입에 내가 누구인지 밝힌다.\n- 서론, 본론, 결론의 구성으로 작성하고 문단별로 줄바꿈을 한다.\n- 문자 내용만 출력한다."},
            {"role": "user", "content": f"1. 수신자 : ${receiver}\n2. 문자 쓰는 목적 : ${purpose}\n3. 문자의 어조 : ${tone}\n4. 추가적인 상황 정보 : ${more_info}"},
        ],
        temperature=0.8,
        max_tokens=2048
    )

    message_result = response["choices"][0]["message"]["content"].encode("utf-8").decode()
    print('message_result : ', message_result)

    return jsonify({"result": message_result})

if __name__ == '__main__':
    app.run(host = '127.0.0.1', debug=True, port=5000)
