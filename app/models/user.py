
from app import db



class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String)
    # email= db.Column(db.String)
    password=db.Column(db.String)
    confirmed_password=db.Column(db.String)
    scores=db.relationship("Score", back_populates="user", lazy=True)
    

    def to_json(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            # 'email': self.email,
            'password':self.password,
            'confirmed_password':self.confirmed_password
            
        }    