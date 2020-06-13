import sys, os
from API.User import User, read_token
import API.googleSignIn  as gs
import API.googleCalendar  as gc
from flask import Flask, jsonify, make_response
from flask_cors import CORS, cross_origin
import logging, json
from flask import Flask, request
from flask_login import LoginManager, login_user
import grpc
from gRPC import indeedclone_pb2, indeedclone_pb2_grpc
from google.protobuf.json_format import MessageToDict
from dotenv import load_dotenv

load_dotenv()
INDEEDCLONE_ENDPOINT = os.getenv("INDEEDCLONE_ENDPOINT")

SECRET_KEY = 'development key'
app = Flask(__name__)
app.secret_key = SECRET_KEY

login_manager = LoginManager()
login_manager.init_app(app)

cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@login_manager.user_loader
def load_user(user_id):
    logging.info('user get done')
    return User.get(user_id)

@app.route('/login', methods=["POST"])  ##exchange token
@cross_origin()
def login():
    google_exchange_token = request.get_json().get("googleExchangeToken")
    google_access_token = request.get_json().get("googleAccessToken")
    user = gs.google_token_verification(google_exchange_token, google_access_token)
    events = gc.get_events(google_access_token, user.email)
    logging.info('calendar events %s', events)
    if (user is not None):
        login_user(user, remember=True)
        try:
            response = jsonify({"ok": True, 'token': user.get_token().decode('utf-8'), 'user':user.user_to_JSON(), 'calendar':json.loads(events)})
        except Exception as e:
            logging.info('error %s', e)

    else:
        response = jsonify({"ok": False, "error": "cannot login or signup"})

    return response


@app.route('/cookielogin', methods=["POST"])
def cookielogin():
    logging.info("start cookie login")

    token = request.get_json().get("jwt")
    decoded =  read_token(token)
    user = gs.token_Login(decoded.get('id'))

    google_access_token = decoded.get('google_access_token')
    email = decoded.get('email')
    events = gc.get_events(google_access_token, email)
    logging.info('calendar events %s', type(events))

    if (user is not None):
        login_user(user, remember=True)
        response = jsonify({"ok": True, 'token': user.get_token().decode('utf-8'), 'user':user.user_to_JSON(), 'calendar': json.loads(events)})
        logging.info("user cookie loggedin %s", user.id)
    else:
        response = jsonify({"ok": False, "token": "", 'user':None})

    return response


@app.route('/addevent', methods=["POST"])
def add_calendar_event():
    logging.info("Adding calendar event")

    token = request.get_json().get("jwt")
    decoded = jwt.decode(token, JWT_SECRET, 'HS256')
    google_access_token = decoded.get('google_access_token')
    email = decoded.get('email')
    print("%s %s", token, email)

    # google_access_token = request.get_json().get("token")
    # email = request.get_json().get("email")
    # event = request.get_json().get("event")
    # print("%s ", event)

    success = gc.add_event(google_access_token, email, event)
    if success is True:
        events = gc.get_events(google_access_token, email)
        response = jsonify({"ok": True, 'calendar': json.loads(events)})
    else:
        response = jsonify({"ok": False})
    return response


@app.route('/indeedclone', methods=["POST"])
def search():
    searchTerm = request.get_json()['term']
    logging.fatal("Start service search term: %s", searchTerm)
    try:
        channel = grpc.insecure_channel(INDEEDCLONE_ENDPOINT)
        stub = indeedclone_pb2_grpc.jobServiceStub(channel)
        res = stub.Search(indeedclone_pb2.searchRequest(term=searchTerm))
        jobList = MessageToDict(res)
        response = jsonify({"ok": True, 'jobList': jobList})
        return response

    except Exception as e:
        print(e)
        return e

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/')
def main():
    return '''<h2>hi Personal Assistant - bakend</h2>'''

if __name__ == "__main__":
    logging.getLogger('flask_cors').level = logging.DEBUG
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)

    app.run(host='0.0.0.0', debug=True)

