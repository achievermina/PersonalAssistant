from app import app
from flask import json
from google.oauth2 import id_token
from google.auth.transport import requests
import configparser

config = configparser.ConfigParser()
config.read('../config.ini')
config.sections()


GOOGLE_CLIENT_ID = config['google']['client_id']
GOOGLE_CLIENT_SECRET = config['google']['client_secret']

# def test_add():
#     response = app.test_client().post(
#         '/add',
#         data=json.dumps({'a': 1, 'b': 2}),
#         content_type='application/json',
#     )
#
#     data = json.loads(response.get_data(as_text=True))
#
#     assert response.status_code == 200
#     assert data['sum'] == 3
#

def test_login():
    response = app.test_client().post(
        '/login',
        data=json.dumps({'googleToken': "", "myToken":""}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))
    print(data)
    assert data['ok'] == True

def test_google_API():
    accessToken ="eyJhbGciOiJSUzI1NiIsImtpZCI6IjUzYzY2YWFiNTBjZmRkOTFhMTQzNTBhNjY0ODJkYjM4MDBjODNjNjMiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwiYXpwIjoiMjYzOTEyODkxNDAyLTYyMWZrcmxoZDliZDcxZTRtZTlmanNlNWp0dnMxMm9qLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwiYXVkIjoiMjYzOTEyODkxNDAyLTYyMWZrcmxoZDliZDcxZTRtZTlmanNlNWp0dnMxMm9qLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTAzMDI0NjkzNjA1MzkzNTAxNDM3IiwiZW1haWwiOiJtaW5hbGVlNjU0M0BnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXRfaGFzaCI6IlVtMW83YXVwVXJYc3N6d3h1NXRmNnciLCJuYW1lIjoiQWNoaWV2ZXIgTGVlIiwicGljdHVyZSI6Imh0dHBzOi8vbGg2Lmdvb2dsZXVzZXJjb250ZW50LmNvbS8tNDVRVjJCaExUUFUvQUFBQUFBQUFBQUkvQUFBQUFBQUFBQUEvQUtGMDVuQXZldVNYYkpzVFRJcXNXM2N6dVBzNzdxUktFZy9zOTYtYy9waG90by5qcGciLCJnaXZlbl9uYW1lIjoiQWNoaWV2ZXIiLCJmYW1pbHlfbmFtZSI6IkxlZSIsImxvY2FsZSI6ImVuIiwiaWF0IjoxNTg1MzUzNjEyLCJleHAiOjE1ODUzNTcyMTIsImp0aSI6ImJiM2U0NmExZDg4NWNiOWY0NjkzNzllZjhlNzNmMGFjMzhmMTliNTUifQ.LEqWjnU3q3BDLF4HBZBSdUL9LqgTpdlOD9aAReNTQNvKMrj4nbF0dqcbagbThQrzDdLy--ALZCiX8YWa960GOhD6naI-4sBPg6d9uDJ9yLaWmXG0AiSca4bjZKmm098UxZh3vO3HsBgFVwfbYO28TWzFVqlh1Jd0LbVvbohd_CkfQWGhoxpYWiD8JtjIkQOtzdRGmGhIL5_EjRLFWUnCdpgWCwGlp_yOdDJ_lf2xKk-DfLtfp88Vm1eaJyGVeYpgNcE_XUhjsYFj7anbWUjPgsKKyPzfnUGTRtRZwhDCqc3XI1UrMOWvDfq2HeC3-WTU_mz5DMzg0B60ZqV613upsQ"
    idinfo = id_token.verify_oauth2_token(accessToken, requests.Request(), GOOGLE_CLIENT_ID)
    print("here", idinfo)
    if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
        assert False
    user_id = idinfo['sub']
    print("accesstoken in google", user_id)
    assert accessToken == user_id

if __name__ == '__main__':
    # test_google_API()
    test_login()
