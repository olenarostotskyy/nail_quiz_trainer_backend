from app import db
from app.models.category import Category



class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String)
    question= db.Column(db.String)
    correct_answer=db.Column(db.String)
    incorrect_answer1=db.Column(db.String)
    incorrect_answer2=db.Column(db.String)
    incorrect_answer3=db.Column(db.String)
    category_id=db.Column(db.Integer, db.ForeignKey('category.category_id'))
    category=db.relationship("Category", back_populates="cards")

    


    def to_json(self):
        return {
            'card_id': self.card_id,
            'category_name': self.category_name,
            'question': self.question,
            'correct_answer':self.correct_answer,
            'incorrect_answer':[self.incorrect_answer1,self.incorrect_answer2, self.incorrect_answer3]  
        }