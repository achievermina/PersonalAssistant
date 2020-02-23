from flask_login import UserMixin
from DataBase.dynamoDB import Database
import logging

class User(UserMixin):
    def __init__(self, id_, name, email):
        self.id = id_
        self.name = name
        self.email = email

    @staticmethod
    def get(user_id):
        try:
            db = Database()
            user =  db.read_item("user-info", "id", user_id)
            user = User(
                id_=user["Item"]["id"], email=user["Item"]["email"]
            )
            return user

        except:
            return None

    @staticmethod
    def create(id, name, email):
        try:
            db = Database()
            item = {"id": id, "email": email}
            db.add_item("user-info", item)
        except:
            logging.info("Adding email: ", email, " failed" )
