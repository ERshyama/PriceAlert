from app import db


class User(db.Model):
    __tablename__ = 'registered_user'
    email = db.Column(db.String(128), primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)

    def __init__(self, email, name):
        self.email = email
        self.name = name
        self.date_created = db.func.current_timestamp()
