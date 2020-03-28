from flask_login import UserMixin
from DataBase.dynamoDB import Database
import jwt
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
config.sections()

class User(UserMixin):
    def __init__(self, user_id, email=None, name=None, authenticated=False):
        self.id = user_id
        self.email = email
        self.name = name
        self.authenticated = authenticated
        self.active = True
        JWT_SECRET = config['JWT']['secret']

    @staticmethod
    def get(user_id):
        try:
            db = Database()
            user =  db.read_item("user-info2", user_id)
            current_user = User(user['id'], user['email'], user['name'], user['authenticated'])
            return current_user

        except:
            return None

    def is_active(self):
        return True

    def is_authenticated(self):
        return self.authenticated

    def get_token(self):
        encoded = jwt.encode({'id': self.id, 'email': self.email}, JWT_SECRET, algorithm='HS256')
        return str(encoded)

    def __repr__(self):
        return " "