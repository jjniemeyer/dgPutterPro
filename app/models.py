from app import app, db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import CheckConstraint
from datetime import datetime
from time import time
import jwt


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    drills = db.relationship('Drill', backref='user', lazy='dynamic')

    current_goal = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time()+expires_in},
            app.config['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)



@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Drill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    putt_distance = db.Column(db.Integer)
    number_attempts = db.Column(db.Integer)
    number_putts_made = db.Column(db.Integer)
    CheckConstraint(number_putts_made <= number_attempts)

    def __repr__(self):
        return '<Drill {}: {} putts out of {} made from {} feet>'.format(self.id, self.number_putts_made,
                                                                           self.number_attempts, self.putt_distance)

