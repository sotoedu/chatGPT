from flask import Flask, request, jsonify, render_template
import openai

openai.api_key = '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'

app = Flask(__name__)

@app.route('/api/chat', methods=['POST'])
def chat():
    message = request.json['message']
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that suggests good restaurants in Jeju."},
            {"role": "user", "content": message}
        ]
    )
    return jsonify(response['choices'][0]['message']['content'])

@app.route('/')
def home():
    return render_template('index.html')

def main():
    app.run(debug=True, host="0.0.0.0", port=5000)

if __name__ == "__main__":
    main()
