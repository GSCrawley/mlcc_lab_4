from flask import Flask, render_template, request
import requests

app = Flask(__name__)
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/question', methods=['POST'])

def question():
    question = str(request.form['question'])
    response = requests.post('http://127.0.0.1:5001/question', json={'question': question})
    if response.status_code == 200:
        result = response.json()['result']
        return f"The result of {question} is: {result}"
    else:
        return "Error occurred while processing the number."

if __name__ == '__main__':
    app.run(debug=True, port=5000)