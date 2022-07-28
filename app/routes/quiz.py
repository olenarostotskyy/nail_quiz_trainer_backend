from flask import Blueprint, jsonify, request, abort, make_response
from app.models.quiz import Quiz
from app import db
from flask import current_app as app
import requests

# "question_id":1,
#         "question":"what is nail polish?",
#         "correct_answer":"nail polish",
#         "incorrect_answers":["answer1","answer2","answer3"]

# questions=[
#     Quiz(1,"what is nail polish?","nail polish","incorrect_answer1","incorrect_answer2","incorrect_answer3"),
#     Quiz(2,"what is nail?","nail","incorrect_answer1","incorrect_answer2","incorrect_answer3"),

# ]

questions_bp = Blueprint('questions_bp', __name__, url_prefix='/questions')

# helper function to validate if request body contains all atributes to post new question
# def check_request_body_for_questions():
#     request_body = request.get_json()
#     if "question" not in request_body or "correct_answer" not in request_body or "incorrect_answer1" not in request_body or "incorrect_answer2" not in request_body or "incorrect_answer3" not in request_body:
#         abort(make_response({"details": f"invalid data: should contain a question,correct and incorrect answers"}, 404))
#     return request_body

def validate_question_id(question_id):
    try:
        question_id = int(question_id)
    except TypeError:
        abort(make_response({"details": "Question ID is invalid data type"}, 400
                            ))
    question = Quiz.query.get(question_id)
    if not question:
        abort(make_response({"details": f"No question with id: {question_id}"}, 404
                            ))
    return question

@questions_bp.route('', methods=['POST'])
def post_new_question():
    new_question_request = request.get_json()
    try:
        new_question = Quiz(question=new_question_request['question'], correct_answer=new_question_request['correct_answer'], incorrect_answer1=new_question_request['incorrect_answer1'], incorrect_answer2=new_question_request['incorrect_answer2'], incorrect_answer3=new_question_request['incorrect_answer3'] )
    except KeyError:
        return {'error details': 'Question, correct answer and incorect answers are required to post a new question'}, 400
    db.session.add(new_question)
    db.session.commit()

    rsp = {'message': f'New question created with id: {new_question.question_id}'}
    return rsp, 201 


#get all questions    
@questions_bp.route('', methods=['GET'])
def get_all_questions():
    questions = Quiz.query.all()
   
    response_body = [question.to_json() for question in questions]

    return jsonify(response_body), 200       
     
#get question by id
@questions_bp.route("/<question_id>",methods=["GET"])
def get_one_question(question_id):
    question=validate_question_id(question_id)
    response_body =   {
            'question_id': question.question_id,
            'question': question.question,
            'correct_answer': question.correct_answer,
            'incorrect_answers':[question.incorrect_answer1,question.incorrect_answer2, question.incorrect_answer3]
        }  
    
    return jsonify(response_body), 200



@questions_bp.route("/<question_id>", methods=["DELETE"])
def delete_question(question_id):
    question = validate_question_id(question_id)
    
    db.session.delete(question)
    db.session.commit()
    
    return { "msg": f"Question {question_id} is successfully deleted." }, 200     

    # questions_response=[]
    #  for question in questions:
    #      questions_response.append({
    #          "question_id":question.question_id,
    #          "question":question.question,
    #          "correct_answer":question.correct_answer,
    #          "incorrect_answers":[question.incorrect_answer1,question.incorrect_answer2,question.incorrect_answer3]
    #      })

    #  return jsonify(questions_response)     


