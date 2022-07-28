from tokenize import String
from app import db
from sqlalchemy.dialects.postgresql import ARRAY


# class Quiz:
#      def __init__(self, question_id, question, correct_answer,incorrect_answer1,incorrect_answer2,incorrect_answer3):
#         self.question_id = question_id
#         self.question = question
#         self.correct_answer = correct_answer
#         self.incorrect_answer1=incorrect_answer1
#         self.incorrect_answer2=incorrect_answer2       
#         self.incorrect_answer3=incorrect_answer3


class Quiz(db.Model):
    question_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.String)
    correct_answer = db.Column(db.String)
    incorrect_answer1=db.Column(db.String)
    incorrect_answer2=db.Column(db.String)
    incorrect_answer3=db.Column(db.String)

    def to_json(self):
        return {
            'question_id': self.question_id,
            'question': self.question,
            'correct_answer': self.correct_answer,
            'incorrect_answers':[self.incorrect_answer1,self.incorrect_answer2, self.incorrect_answer3]
        }
    # incorrect_answers=db.Column(db.ARRAY(String))