from flask_login import UserMixin
from DataBase.dynamoDB import Database
import logging
import json

class User(UserMixin):
    def __init__(self, user):
        # currentUser = json.loads(user)
        # self.id = currentUser['id']
        # self.name = currentUser['name']
        # self.email = currentUser['email']
        # self.accessToken = currentUser['accessToken']
        # self.idToken = currentUser['idToken']
        # self.expires_at = currentUser['expires_at']
        pass

    @staticmethod
    def get(user_id, user_email):
        try:
            db = Database()
            user =  sdb.read_item("user-info", "id", user_id)
            user = User(
                id_=user["Item"]["id"], email=user["Item"]["email"]
            )

            if (user.email == user_email):
                return user

        except:
            return None

    @staticmethod
    def create(id, name, email):
        try:
            db = Database()
            item = {"id": id, "email": email}
            db.add_item("user-info", item)
            return True
        except:
            logging.info("Adding email: ", email, " failed" )
