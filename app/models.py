from app import db
from datetime import datetime





class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    mobile = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    verify_code = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(200), unique=True, nullable=False)
    is_verified = db.Column(db.Boolean(), default=0)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow,
                           onupdate=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' %self.first_name
