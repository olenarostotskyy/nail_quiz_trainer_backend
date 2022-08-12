from app import db



class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    cards=db.relationship("Card", back_populates="category", lazy=True)
    


    def to_json(self):
        return {
            'category_id': self.category_id,
            'name': self.name,
            
        }