import getpass
from DataBase.dynamoDB import Database
import json, requests
from API.User import User
from flask import jsonify, request
import configparser
from oauthlib.oauth2 import WebApplicationClient


config = configparser.ConfigParser()
config.read('config.ini')
config.sections()



GOOGLE_CLIENT_ID = config['google']['client_id']
GOOGLE_CLIENT_SECRET = config['google']['client_secret']
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

client = WebApplicationClient(GOOGLE_CLIENT_ID)

def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()


def check_authentication(currentUser):
    # retrieve user information
    # requestUser = json.loads(user)
    id = currentUser['id']
    name = currentUser['name']
    email = currentUser['email']
    accessToken = currentUser['accessToken']
    idToken = currentUser['idToken']
    expires_at = currentUser['expires_at']
    result = ""

    # check DB
    dbUser = User.get(email, id)

    # if user exists -> login
    # if user not exist or no token, google authentication again
    # then create/update user
    if dbUser is None:
        if (check_email_verification(currentUser) and User.create(currentUser)):
            return User.get(email, id)
        else:
            return None
    else:
        return dbUser


## Maybe error here
def check_email_verification(currentUser):
    code = request.args.get("code")
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response= request.url,
        redirect_url= request.base_url,
        code=code,
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    #Parse the token
    client.parse_request_body_response(json.dumps(token_response.json()))
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    print(userinfo_response.json())
    if userinfo_response.json().get("email_verified"):
        return True
    else:
        return False

