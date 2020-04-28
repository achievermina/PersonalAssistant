import sys

from DataBase.dynamoDB import Database
from API.User import User
import API.googleSignIn  as gs
import API.googleCalandar  as gc
from flask import Flask, jsonify, make_response
from flask_cors import CORS, cross_origin
import logging, json
from flask import Flask, redirect, url_for, session, render_template, request
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
import grpc
from gRPC import indeedclone_pb2, indeedclone_pb2_grpc

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

@app.route('/login', methods=["POST"])
@cross_origin()
def login():
    googleToken = request.get_json().get("googleToken")
    user = gs.google_token_verification(googleToken)

    if (user is not None):
        login_user(user, remember=True)
        try:
            response = jsonify({"ok": True, 'token': user.get_token().decode('utf-8'), 'user':user.toJSON()})
        except Exception as e:
            logging.info('error %s', e)

    else:
        response = jsonify({"ok": False, "error": "cannot login or signup"})

    return response


@app.route('/cookielogin', methods=["POST"])
def cookielogin():
    token = request.get_json().get("jwt")
    logging.info("getting encoded token %s type %s", token, type(token))
    user = gs.token_Login(token)

    if (user is not None):
        login_user(user, remember=True)
        response = jsonify({"ok": True, "token": user.get_token().decode('utf-8'), 'user':user.toJSON()})
        logging.info("user cookie loggedin %s", user.id)
    else:
        response = jsonify({"ok": False, "token": "", 'user':None})

    return response


@app.route('/calendar', methods=["GET"])
def get_calendar():
    print("calendar here")

    if session.get('logged_in') is not None:
        calendar = gc.GoogleCanlandarAPI()
    else:
        return jsonify({"ok": False, "error": "cannot login or signup"})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/')
def main():
    return '''<h2>hi</h2>'''

@app.route('/indeedclone',methods=["POST"])
def search():
    logging.fatal("Start service")
    searchTerm = request.get_json()["term"]
    try:
      channel = grpc.insecure_channel('0.0.0.0:3000')
      stub = indeedclone_pb2_grpc.jobServiceStub(channel)
      response = stub.Search(indeedclone_pb2.searchRequest(term=searchTerm))
      return response

    except Exception as e:
      print(e)
      return e


@app.route('/test-items')
def test_items():
    db = Database()
    return '''<h2>db.test_db()</h2>'''


@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify({'sum': int(data['a']) + int(data['b'])})

if __name__ == "__main__":
    logging.getLogger('flask_cors').level = logging.DEBUG
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)

    app.run(host='0.0.0.0', debug=True)

