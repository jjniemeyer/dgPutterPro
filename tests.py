from datetime import datetime, timedelta
import unittest
from app import create_app, db
from app.models import User, Drill
from config import Config

class TestConfig(Config):
    TESTING = True # currently not used but may be useful
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        u = User(username='joe')
        u.set_password('mamma')
        self.assertFalse(u.check_password('pappa'))
        self.assertTrue(u.check_password('mamma'))

        ## find more things to test in UserModel
        ## test that user sees all drills with their user id?


if __name__ == '__main__':
    unittest.main(verbosity=2)