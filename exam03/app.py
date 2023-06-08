import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    try :
        if request.method == "POST":
            animal = request.form["animal"]
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=generate_prompt(animal),
                temperature=0.6,
                n=3
            )
            return redirect(url_for("index", result=response.choices[0].text))

        result = request.args.get("result")
        return render_template("index.html", result=result)
    except Exception as Err :

        return render_template("index.html", result='다시 요청해 주세요.')


def generate_prompt(animal):
    return """펫의 이름을 한국어로 추천 해 줘 {}""".format(
        animal.capitalize()
    )
