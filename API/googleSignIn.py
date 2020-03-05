from DataBase.dynamoDB import Database
import logging, jwt
from API.User import User
import configparser
from google.oauth2 import id_token
from google.auth.transport import requests

config = configparser.ConfigParser()
config.read('./config.ini')
config.sections()


GOOGLE_CLIENT_ID = config['google']['client_id']
GOOGLE_CLIENT_SECRET = config['google']['client_secret']
JWT_SECRET = config['JWT']['secret']

idinfo = {'sub':"103024693605393501437", 'email':'hhhhhhheheheh@gmail.com', "name":"missssna", "expires_at":123, "email_verified":False}

def google_token_verification(accessToken):
    try:
        print("accesstoken in gs", accessToken)
        idinfo = id_token.verify_oauth2_token(accessToken, requests.Request(), GOOGLE_CLIENT_ID)
        print("here", idinfo)
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')
        user_id = idinfo['sub']
        print("accesstoken in google", user_id)

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
            print("user added :", user)

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

def token_Login(myToken): ## 그냥 토큰자체를 저장하고 토큰이 같은지 확인? 아니면 해독해서 확인?
    decoded = jwt.decode(myToken, JWT_SECRET, algorithms=['HS256'])
    user = User.get(decoded["id"])
    if user is not None:
        return user


def generate_myToken():
    pass
