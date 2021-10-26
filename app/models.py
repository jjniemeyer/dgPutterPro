from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import  CheckConstraint
from datetime import datetime



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

