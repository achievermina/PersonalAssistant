from flask_login import UserMixin
from DataBase.dynamoDB import Database
import jwt, logging, json, os
from dotenv import load_dotenv

load_dotenv()
JWT_SECRET = os.getenv("JWT_SECRET")

class User(UserMixin):
    def __init__(self, user_id, email=None, name=None, email_verified=False,
                 google_access_token=None, google_calendar_next_sync_token = None):
        self.id = user_id
        self.email = email
        self.name = name
        self.email_verified = email_verified
        self.google_access_token = google_access_token
        self.google_calendar_next_sync_token = google_calendar_next_sync_token
        self.active = True

    @staticmethod
    def get(user_id):
        logging.info("getting user from the database %s", user_id )
        try:
            db = Database()
            user =  db.read_item("user-info", user_id)
            if user is None:
                logging.error("getting user from the database is NONE")
                return None
            current_user = User(user['id'], user['email'], user['name'], user['email_verified'],
                                user['google_access_token'], user['google_calendar_next_sync_token'])
            return current_user

        except:
            return None

    def save_next_sync_token(self, user_google_calendar_next_sync_token):
        logging.info("Saving user google calendar next sync token to the database %s",
                     user_google_calendar_next_sync_token)
        try:
            db = Database()
            db.update_item("user-info", self.id, "google_calendar_next_sync_token",
                           user_google_calendar_next_sync_token)
            return True
        except:
            return False

    def get_next_sync_token(self):
        return self.google_calendar_next_sync_token

    def get_google_access_token(self):
        return self.google_access_token

    def is_active(self):
        return True

    def is_authenticated(self):
        return self.email_verified

    def get_token(self):
        encoded = jwt.encode({'id': self.id, 'email': self.email, 'google_access_token': self.google_access_token,
                              'google_calendar_next_sync_token': self.google_calendar_next_sync_token},
                             JWT_SECRET,
                             algorithm='HS256')
        logging.info("encode type %s", type(encoded))
        return encoded

    def user_to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def __repr__(self):
        return self.user_to_JSON()

def read_token(myToken):
    decoded = jwt.decode(myToken, JWT_SECRET, 'HS256')
    return decoded