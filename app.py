from DataBase.dynamoDB import Database
from API.User import User
import logging, json, requests, os
import configparser
from flask import Flask, redirect, url_for, session, render_template, request
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from oauthlib.oauth2 import WebApplicationClient

config = configparser.ConfigParser()
config.read('config.ini')
config.sections()

GOOGLE_CLIENT_ID = config['google']['client_id']
GOOGLE_CLIENT_SECRET = config['google']['client_secret']
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

SECRET_KEY = 'development key'

app = Flask(__name__)
app.secret_key = SECRET_KEY

login_manager = LoginManager()
login_manager.init_app(app)
client = WebApplicationClient(GOOGLE_CLIENT_ID)

def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()


@login_manager.user_loader
def load_user(user_id):
    logging.info('user get done')
    return User.get(user_id)

@app.route("/")
def index():
    if current_user.is_authenticated:
        logging.info("logged in")
        return (
            "<p>Hello, {}! You're logged in! Email: {}</p>"
            '<a class="button" href="/logout">Logout</a>'.format(
                current_user.id, current_user.email
            )
        )
    else:
        return '<a class="button" href="/login">Google Login</a>'

@app.route('/login')
def login():
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]
    logging.info(' authorization_endpoint done')

    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri= request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    logging.info(' request_uri done')
    return redirect(request_uri)

@app.route("/login/callback")
def callback():
    code = request.args.get("code")
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
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
    logging.info(' callback get')
    print(userinfo_response.json())
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400

    # Create a user in your db with the information provided
    user = User(
        id_=unique_id, name=users_name, email=users_email
    )
    logging.info(' adding user ')

    if not User.get(unique_id):
        User.create(unique_id, users_name, users_email)
        logging.info(' adding user done')

    ### After saving the user information, not able to keep the login
    login_user(user)

    return redirect(url_for("index"))


########################################################

@app.route('/test-items')
def test_items():
    db = Database()
    return '''<h2>db.test_db()</h2>'''


@app.route('/google')
def signIn():
    return render_template('googleSignIn.html')


@app.route('/mainmain')
def main():
    return render_template("main.html")


if __name__ == "__main__":
    app.run(ssl_context="adhoc")
