from flask_login import UserMixin
from DataBase.dynamoDB import Database
import logging
import json

class User(UserMixin):
    def __init__(self, user_id, email=None, name=None, authenticated=False):
        self.id = user_id
        self.email = email
        self.name = name
        self.authenticated = authenticated
        self.active = True

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

    def __repr__(self):
        return " "