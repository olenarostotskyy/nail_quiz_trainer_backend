from flask import Blueprint, jsonify, request, abort, make_response
from app.models.user import User
from app.models. score import Score
from app import db
from flask import current_app as app
import requests

users_bp = Blueprint('users_bp', __name__, url_prefix='/users')


# helper function to validate if request body contains all the info
def check_request_body_for_score():
    request_body = request.get_json()
    if "score" not in request_body:
        abort(make_response({"details": f"invalid data: should contain a score"}, 404))
    return request_body


def validate_user_id(user_id):
    try:
        user_id = int(user_id)
    except TypeError:
        abort(make_response({"details": "User ID is invalid data type"}, 400
                            ))
    user = User.query.get(user_id)
    if not user:
        abort(make_response({"details": f"No user with id: {user_id}"}, 404
                            ))
    return user

@users_bp.route('', methods=['POST'])
def post_new_user():
    new_user_request = request.get_json()
    try:
        new_user = User(username = new_user_request['username'], email=new_user_request['email'], password=new_user_request['password'], confirmed_password=new_user_request['confirmed_password'])
    except KeyError:
        return {'error details': 'Username, email and password are required to post a new user'}, 400
    db.session.add(new_user)
    db.session.commit()

    rsp = {'message': f'New user created with id: {new_user.user_id}'}
    return rsp, 201 


#get all users    
@users_bp.route('', methods=['GET'])
def get_all_users():
    users = User.query.all()
   
    response_body = [user.to_json() for user in users]

    return jsonify(response_body), 200       
     

#get user by id
@users_bp.route("/<user_id>",methods=["GET"])
def get_one_user(user_id):
    user=validate_user_id(user_id)
    response_body =   {
            'user_id': user.user_id,
            'username': user.username,
            'email': user.email,
            'confirmed_password':user.confirmed_password
        }  
    
    return jsonify(response_body), 200


# delete user
@users_bp.route("/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = validate_user_id(user_id)
    
    db.session.delete(user)
    db.session.commit()
    
    return { "msg": f"User {user_id} is successfully deleted." }, 200     


# post score for specific user id
@users_bp.route("/<user_id>/score", methods=["POST"])
def create_score_for_user(user_id):
    request_body = check_request_body_for_score()
    user = validate_user_id(user_id)
    new_score = Score(score=request_body["score"] )
    user.scores.append(new_score)
    db.session.commit()
    
    response = new_score.to_json()
    return jsonify(response), 201

# get all score for specific user id
@users_bp.route("/<user_id>/score", methods=["GET"])   
def get_all_scores_from_user(user_id):
    user = validate_user_id(user_id)
    scores = user.scores
    list_all_scores = [score.to_json() for score in scores]
    
    return jsonify(list_all_scores), 200