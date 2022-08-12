from unicodedata import category
from flask import Blueprint, jsonify, request, abort, make_response
from app.models.category import Category
from app import db
from flask import current_app as app
import requests

categories_bp = Blueprint('categories_bp', __name__, url_prefix='/categories')

def validate_category_id(category_id):
    try:
        category_id = int(category_id)
    except TypeError:
        abort(make_response({"details": "Category ID is invalid data type"}, 400
                            ))
    category = Category.query.get(category_id)
    if not category:
        abort(make_response({"details": f"No category with id: {category_id}"}, 404
                            ))
    return category

@categories_bp.route('', methods=['POST'])
def post_new_category():
    new_category_request = request.get_json()
    try:
        new_category_request = Category(name=new_category_request['name'] )
    except KeyError:
        return {'error details': 'Name is required to post a new category'}, 400
    
    db.session.add(new_category_request)
    db.session.commit()

    rsp = {'message': f'New category created with : {new_category_request.category_id}'}
    return rsp, 201 


#get all categories    
@categories_bp.route('', methods=['GET'])
def get_all_categories():
    categories = Category.query.all()
   
    response_body = [category.to_json() for category in categories]

    return jsonify(response_body), 200       
     
#get category by id
# @questions_bp.route("/<category_id>",methods=["GET"])
# def get_one_question(category_id):
#     category=validate_question_id(category_id)
#     response_body =   {
#             'category_id': category.category_id,
#             'category': category.category,
#             'correct_answer': category.correct_answer,
#             'incorrect_answers':[category.incorrect_answer1,category.incorrect_answer2, category.incorrect_answer3]
#         }  
    
#     return jsonify(response_body), 200



@categories_bp.route("/<category_id>", methods=["DELETE"])
def delete_card(category_id):
    category =validate_category_id(category_id)
    
    db.session.delete(category)
    db.session.commit()
    
    return { "msg": f"Category {category_id} is successfully deleted." }, 200  