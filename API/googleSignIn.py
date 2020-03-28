from DataBase.dynamoDB import Database
import logging, jwt
from API.User import User
import configparser
from google.oauth2 import id_token
from google.auth.transport import requests

config = configparser.ConfigParser()
config.read('../config.ini')
config.sections()

idinfo = {'sub':"103024693605393501437", 'email':'hhhhhhheheheh@gmail.com', "name":"missssna", "expires_at":123, "email_verified":False}

def google_token_verification(accessToken):
    GOOGLE_CLIENT_ID = config['google']['client_id']
    GOOGLE_CLIENT_SECRET = config['google']['client_secret']

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

# def token_Login(myToken): ## 그냥 토큰자체를 저장하고 토큰이 같은지 확인? 아니면 해독해서 확인?
#     decoded = jwt.decode(myToken, JWT_SECRET, algorithms=['HS256'])
#     user = User.get(decoded["id"])
#     if user is not None:
#         return user


def generate_myToken():
    pass

if __name__ == "__main__":
    accessToken ="eyJhbGciOiJSUzI1NiIsImtpZCI6IjUzYzY2YWFiNTBjZmRkOTFhMTQzNTBhNjY0ODJkYjM4MDBjODNjNjMiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwiYXpwIjoiMjYzOTEyODkxNDAyLTYyMWZrcmxoZDliZDcxZTRtZTlmanNlNWp0dnMxMm9qLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwiYXVkIjoiMjYzOTEyODkxNDAyLTYyMWZrcmxoZDliZDcxZTRtZTlmanNlNWp0dnMxMm9qLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTAzMDI0NjkzNjA1MzkzNTAxNDM3IiwiZW1haWwiOiJtaW5hbGVlNjU0M0BnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXRfaGFzaCI6IlVtMW83YXVwVXJYc3N6d3h1NXRmNnciLCJuYW1lIjoiQWNoaWV2ZXIgTGVlIiwicGljdHVyZSI6Imh0dHBzOi8vbGg2Lmdvb2dsZXVzZXJjb250ZW50LmNvbS8tNDVRVjJCaExUUFUvQUFBQUFBQUFBQUkvQUFBQUFBQUFBQUEvQUtGMDVuQXZldVNYYkpzVFRJcXNXM2N6dVBzNzdxUktFZy9zOTYtYy9waG90by5qcGciLCJnaXZlbl9uYW1lIjoiQWNoaWV2ZXIiLCJmYW1pbHlfbmFtZSI6IkxlZSIsImxvY2FsZSI6ImVuIiwiaWF0IjoxNTg1MzUzNjEyLCJleHAiOjE1ODUzNTcyMTIsImp0aSI6ImJiM2U0NmExZDg4NWNiOWY0NjkzNzllZjhlNzNmMGFjMzhmMTliNTUifQ.LEqWjnU3q3BDLF4HBZBSdUL9LqgTpdlOD9aAReNTQNvKMrj4nbF0dqcbagbThQrzDdLy--ALZCiX8YWa960GOhD6naI-4sBPg6d9uDJ9yLaWmXG0AiSca4bjZKmm098UxZh3vO3HsBgFVwfbYO28TWzFVqlh1Jd0LbVvbohd_CkfQWGhoxpYWiD8JtjIkQOtzdRGmGhIL5_EjRLFWUnCdpgWCwGlp_yOdDJ_lf2xKk-DfLtfp88Vm1eaJyGVeYpgNcE_XUhjsYFj7anbWUjPgsKKyPzfnUGTRtRZwhDCqc3XI1UrMOWvDfq2HeC3-WTU_mz5DMzg0B60ZqV613upsQ"
    google_token_verification(accessToken)