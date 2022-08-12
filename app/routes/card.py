from flask import Blueprint, jsonify, request, abort, make_response
from app.models.card import Card
from app import db
from flask import current_app as app
import requests

cards_bp = Blueprint('cards_bp', __name__, url_prefix='/cards')

def validate_card_id(card_id):
    try:
        card_id = int(card_id)
    except TypeError:
        abort(make_response({"details": "Card ID is invalid data type"}, 400
                            ))
    card = Card.query.get(card_id)
    if not card:
        abort(make_response({"details": f"No card with id: {card_id}"}, 404
                            ))
    return card

@cards_bp.route('', methods=['POST'])
def post_new_card():
    new_card_request = request.get_json()
    try:
        new_card = Card(category=new_card_request['category'], question=new_card_request['question'], correct_answer=new_card_request['correct_answer'], incorrect_answer1=new_card_request['incorrect_answer1'], incorrect_answer2=new_card_request['incorrect_answer2'], incorrect_answer3=new_card_request['incorrect_answer3'] )
    except KeyError:
        return {'error details': 'Question, correct answer and incorect answers are required to post a new card'}, 400
    
    db.session.add(new_card)
    db.session.commit()

    rsp = {'message': f'New card created witcard.card_id: {new_card.card_id}'}
    return rsp, 201 


#get all cards    
@cards_bp.route('', methods=['GET'])
def get_all_cards():
    cards = Card.query.all()
   
    response_body = [card.to_json() for card in cards]

    return jsonify(response_body), 200       
     
#get card by id
# @questions_bp.route("/<card_id>",methods=["GET"])
# def get_one_question(card_id):
#     card=validate_question_id(card_id)
#     response_body =   {
#             'card_id': card.card_id,
#             'card': card.card,
#             'correct_answer': card.correct_answer,
#             'incorrect_answers':[card.incorrect_answer1,card.incorrect_answer2, card.incorrect_answer3]
#         }  
    
#     return jsonify(response_body), 200



@cards_bp.route("/<card_id>", methods=["DELETE"])
def delete_card(card_id):
    card = validate_card_id(card_id)
    
    db.session.delete(card)
    db.session.commit()
    
    return { "msg": f"Card {card_id} is successfully deleted." }, 200    