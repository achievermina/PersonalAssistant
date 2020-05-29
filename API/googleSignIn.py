from DataBase.dynamoDB import Database
import logging, jwt
from API.User import User
import configparser
from google.oauth2 import id_token
from google.auth.transport import requests
import os, sys
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
        logging.info("accessToken in google %s", accessToken)
        # logging.info("idinfo in google %s", idinfo)
    except ValueError:
        return

    user = User.get(user_id)
    logging.info("user get: %s", user)
    if user is None:
        newUser = {
            "id":  idinfo["sub"],
            "accessToken": accessToken,
            "email": idinfo["email"],
            "name": idinfo["name"],
            "expires_at": idinfo["exp"],
            "authenticated": idinfo["email_verified"]
        }
        if add_user_to_database(newUser):
            user = User.get(user_id)
            logging.info("database user added : %s, id type %s", user.get_id(), type(user_id) )
        else:
            return
    return user

def add_user_to_database(user):
    try:
        db = Database()
        db.add_item("user-info", user)
        logging.info("Success: adding a new user to DB")
        return True
    except Exception as e:
        logging.info("Adding email: ", user['email'], " failed" , "error", e)

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

if __name__ == "__main__":
    accessToken ="eyJhbGciOiJSUzI1NiIsImtpZCI6IjUzYzY2YWFiNTBjZmRkOTFhMTQzNTBhNjY0ODJkYjM4MDBjODNjNjMiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwiYXpwIjoiMjYzOTEyODkxNDAyLTYyMWZrcmxoZDliZDcxZTRtZTlmanNlNWp0dnMxMm9qLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwiYXVkIjoiMjYzOTEyODkxNDAyLTYyMWZrcmxoZDliZDcxZTRtZTlmanNlNWp0dnMxMm9qLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTAzMDI0NjkzNjA1MzkzNTAxNDM3IiwiZW1haWwiOiJtaW5hbGVlNjU0M0BnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXRfaGFzaCI6IlVtMW83YXVwVXJYc3N6d3h1NXRmNnciLCJuYW1lIjoiQWNoaWV2ZXIgTGVlIiwicGljdHVyZSI6Imh0dHBzOi8vbGg2Lmdvb2dsZXVzZXJjb250ZW50LmNvbS8tNDVRVjJCaExUUFUvQUFBQUFBQUFBQUkvQUFBQUFBQUFBQUEvQUtGMDVuQXZldVNYYkpzVFRJcXNXM2N6dVBzNzdxUktFZy9zOTYtYy9waG90by5qcGciLCJnaXZlbl9uYW1lIjoiQWNoaWV2ZXIiLCJmYW1pbHlfbmFtZSI6IkxlZSIsImxvY2FsZSI6ImVuIiwiaWF0IjoxNTg1MzUzNjEyLCJleHAiOjE1ODUzNTcyMTIsImp0aSI6ImJiM2U0NmExZDg4NWNiOWY0NjkzNzllZjhlNzNmMGFjMzhmMTliNTUifQ.LEqWjnU3q3BDLF4HBZBSdUL9LqgTpdlOD9aAReNTQNvKMrj4nbF0dqcbagbThQrzDdLy--ALZCiX8YWa960GOhD6naI-4sBPg6d9uDJ9yLaWmXG0AiSca4bjZKmm098UxZh3vO3HsBgFVwfbYO28TWzFVqlh1Jd0LbVvbohd_CkfQWGhoxpYWiD8JtjIkQOtzdRGmGhIL5_EjRLFWUnCdpgWCwGlp_yOdDJ_lf2xKk-DfLtfp88Vm1eaJyGVeYpgNcE_XUhjsYFj7anbWUjPgsKKyPzfnUGTRtRZwhDCqc3XI1UrMOWvDfq2HeC3-WTU_mz5DMzg0B60ZqV613upsQ"
    google_token_verification(accessToken)