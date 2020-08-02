from DataBase.dynamoDB import Database
import logging, os
from API.User import User
from google.oauth2 import id_token
from google.auth.transport import requests
from dotenv import load_dotenv

load_dotenv()

def google_token_verification(idToken, accessToken):
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")

    try:
        idinfo = id_token.verify_oauth2_token(idToken, requests.Request(), GOOGLE_CLIENT_ID)
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')
        user_id = idinfo['sub']
        logging.info("idToken in google %s", user_id)
    except ValueError:
        return

    user = User.get(user_id)
    logging.info("user get: %s", user)

    if user is None:
        newUser = {
            "id":  idinfo["sub"],
            "google_access_token": accessToken,
            "email": idinfo["email"],
            "name": idinfo["name"],
            "expires_at": idinfo["exp"],
            "email_verified": idinfo["email_verified"],
            "google_calendar_next_sync_token": None
        }

        if add_user_to_database(newUser):
            user = User.get(user_id)
            logging.error("database user added : %s, id type %s", user.get_id(), type(user_id) )
        else:
            logging.error("database user adding failed")
            return
    return user

def add_user_to_database(user):
    try:
        db = Database()
        logging.error("db %s", db)
        db.add_item("user-info", user)
        logging.error("Success: adding a new user to DB")
        return True
    except Exception as e:
        logging.error("Adding email: ", user['email'], " failed" , "error", e)

    return False

def token_Login(id):
    logging.info("token_Login start")
    try:
        user = User.get(id)
        logging.info("Success: current active user  %s", user.get_id())
        return user
    except Exception as e:
        logging.info("Failed: Token user loading - error: ", e)
        return None