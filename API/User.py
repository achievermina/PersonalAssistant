from flask_login import UserMixin
from DataBase.dynamoDB import Database
import jwt, logging, json
import os
from dotenv import load_dotenv

load_dotenv()
JWT_SECRET = os.getenv("JWT_SECRET")

class User(UserMixin):
    def __init__(self, user_id, email=None, name=None, authenticated=False, accessToken=None):
        self.id = user_id
        self.email = email
        self.name = name
        self.authenticated = authenticated
        self.accessToken = accessToken
        self.active = True

    @staticmethod
    def get(user_id):
        logging.info("getting user from the database %s", user_id )
        try:
            db = Database()
            user =  db.read_item("user-info", user_id)
            if user is None:
                return None
            current_user = User(user['id'], user['email'], user['name'], user['authenticated'], user['accessToken'])
            return current_user

        except:
            return None

    def is_active(self):
        return True

    def is_authenticated(self):
        return self.authenticated

    def get_token(self):
        logging.info("JWT_SECRET %s, type %s", JWT_SECRET,type(JWT_SECRET))

        encoded = jwt.encode({'id': self.id, 'email': self.email, 'accessToken': self.accessToken}, JWT_SECRET, algorithm='HS256')
        logging.info("encode type %s", type(encoded))
        return encoded


    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def __repr__(self):
        return " "

def read_token(myToken):
    decoded = jwt.decode(myToken, JWT_SECRET, 'HS256')
    return decoded