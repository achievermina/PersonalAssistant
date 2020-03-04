from DataBase.dynamoDB import Database
import logging
from API.User import User
import configparser
from google.oauth2 import id_token
from google.auth.transport import requests

config = configparser.ConfigParser()
config.read('./config.ini')
config.sections()


GOOGLE_CLIENT_ID = config['google']['client_id']
GOOGLE_CLIENT_SECRET = config['google']['client_secret']

idinfo = {'sub':"555", 'email':'hi@gmail.com', "name":"mina", "expires_at":123}

def google_token_verification(accessToken):
    try:
        print("accesstoken in gs", accessToken)
        # idinfo = id_token.verify_oauth2_token(accessToken, requests.Request(), GOOGLE_CLIENT_ID)
        #
        # if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
        #     raise ValueError('Wrong issuer.')
        # user_id = idinfo['sub']

    except ValueError:
        return

    user = User.get(user_id)
    print("user get:", user)
    if user is None:
        newUser = {
            "id":  idinfo["sub"],
            "email": idinfo["email"],
            "name": idinfo["name"],
            "expires_at": idinfo["expires_at"],
            "authenticated": idinfo["email_verified"]
        }
        if add_user_to_database(newUser):
            user = User.get(user_id)
        else:
            return
    return user

def add_user_to_database(user):
    try:
        db = Database()
        db.add_item("user-info2", user)
        return True
    except:
        logging.info("Adding email: ", user['email'], " failed" )

    return False