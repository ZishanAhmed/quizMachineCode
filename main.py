from flask import Flask, jsonify, request
from models.question import question
from models.quiz import quiz

app = Flask(__name__)

quiz_list = []
questions_list = []

@app.route('/createQuiz', methods = ['POST'])
def createQuiz():
    data = {}
    return jsonify(data)

@app.route('/createQuestion', methods = ['POST'])
def createQuestion():
    request_data = request.get_json()
    name = request_data['name']
    description = request_data['description']
    options = request_data['options']
    id = request_data['id']
    objQuestion = question(id,name, description, options)
    questions_list.append(objQuestion)
    data = {}
    data["question_id"] = objQuestion.get_question_id()
    data["message"] = "Question created Successfully"
    return jsonify(data)

@app.route('/createAnswer', methods = ['POST'])
def createAnswer():
    data = {}
    return jsonify(data)

@app.route('/listQuiz/')
def listQuiz():
    page_size = request.args.get('page_size')
    offset = request.args.get('offset')
    data = {}
    return jsonify(data)


if __name__ == '__main__':
    print("app is running")
    app.run(debug=True)