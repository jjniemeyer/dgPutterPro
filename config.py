import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir,  '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DATABASE_URL = 'postgres+psycopg2://{user}:{pwd}@{url}/{db}'.format(
        user=os.environ.get('POSTGRES_USER'),
        pwd=os.environ.get('POSTGRES_PWD'),
        url=os.environ.get('POSTGRES_URL'),
        db=os.environ.get('POSTGRES_DB'),
    )
    SQLALCHEMY_DATABASE_URI = DATABASE_URL or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['jani5714@colorado.edu', 'fake.app.real.server@gmail.com']
    DRILLS_PER_PAGE = 10