from app import db



class Score(db.Model):
    score_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    score=db.Column(db.String)
    user_id=db.Column(db.Integer, db.ForeignKey('user.user_id'))
    user=db.relationship("User", back_populates="scores")

    

    def to_json(self):
        return {
            'score_id': self.score_id,
            'score': self.score,
            'user_id':self.user_id
            
        }