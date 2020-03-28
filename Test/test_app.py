from app import app
from flask import json
from google.oauth2 import id_token
from google.auth.transport import requests
import configparser

config = configparser.ConfigParser()
config.read('./config.ini')
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
    accessToken = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjE3ZDU1ZmY0ZTEwOTkxZDZiMGVmZDM5MmI5MWEzM2U1NGMwZTIxOGIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwiYXpwIjoiMjYzOTEyODkxNDAyLTYyMWZrcmxoZDliZDcxZTRtZTlmanNlNWp0dnMxMm9qLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwiYXVkIjoiMjYzOTEyODkxNDAyLTYyMWZrcmxoZDliZDcxZTRtZTlmanNlNWp0dnMxMm9qLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTAzMDI0NjkzNjA1MzkzNTAxNDM3IiwiZW1haWwiOiJtaW5hbGVlNjU0M0BnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXRfaGFzaCI6Il9TVDh1Ni1YeFhEbFlGS1dYWUVQYnciLCJuYW1lIjoiQWNoaWV2ZXIgTGVlIiwicGljdHVyZSI6Imh0dHBzOi8vbGg2Lmdvb2dsZXVzZXJjb250ZW50LmNvbS8tNDVRVjJCaExUUFUvQUFBQUFBQUFBQUkvQUFBQUFBQUFBQUEvQUtGMDVuQXZldVNYYkpzVFRJcXNXM2N6dVBzNzdxUktFZy9zOTYtYy9waG90by5qcGciLCJnaXZlbl9uYW1lIjoiQWNoaWV2ZXIiLCJmYW1pbHlfbmFtZSI6IkxlZSIsImxvY2FsZSI6ImVuIiwiaWF0IjoxNTgzNDY2NTg4LCJleHAiOjE1ODM0NzAxODgsImp0aSI6ImY4ZTVkYjE3ZTA0ZTIyYTNlZmI1OTM0MTZmNTM4Zjg1MTA2NTA4MTYifQ.fW5zpLXoG2PPb6GsuxMDhCR73j1IDNwtw50ZqMNIpVnw9BxgghsA4ugLkyZ32Y42C2S7_mm7KlkDnXOKZ--lEvPHWRvV8peX_f17DCMnDmI0gfTmH84TdLvUcTDorbyjA4BBvdIoQdUKX00BwHBv1XLsSFPh1X44D1PjGKzgyinCqN8nN87W2RJ3T96WPHnzEABkxP8whyCj6zz-Qc__q48XirBxCF0xYMBuUZtdsBJLdPHN1IWaZYNfDQ9a5LPq0uPN5YWcnT10AShGuY2S2qqc_ImwPsOvX4s3OrG2UpP3D0DbkL7zPA67Cuant1HFv3B9DZGCc_07F5xceGm4Cw"
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
