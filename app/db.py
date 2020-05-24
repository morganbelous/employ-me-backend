from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Job(db.Model):
    __tablename__ = 'job'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    name = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False)
    price = db.Column(db.String, nullable = False)
    bio = db.Column(db.String, nullable = False)
    imageName = db.Column(db.String, nullable = False)

    def __init__(self, **kwargs):
        self.title = kwargs.get('title', '')
        self.name = kwargs.get('name', '')
        self.email = kwargs.get('email', '')
        self.price = kwargs.get('price', '')
        self.bio = kwargs.get('bio', '')
        self.imageName = kwargs.get('imageName', '')

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'name': self.name,
            'email': self.email,
            'price': self.price,
            'bio': self.bio,
            'imageName': self.imageName    
        }
